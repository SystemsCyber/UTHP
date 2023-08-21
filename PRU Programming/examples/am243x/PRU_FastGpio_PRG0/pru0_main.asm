; Copyright (C) 2018 Texas Instruments Incorporated - http://www.ti.com/
;
; Redistribution and use in source and binary forms, with or without
; modification, are permitted provided that the following conditions
; are met:
;
; Redistributions of source code must retain the above copyright
; notice, this list of conditions and the following disclaimer.
;
; Redistributions in binary form must reproduce the above copyright
; notice, this list of conditions and the following disclaimer in the
; documentation and/or other materials provided with the
; distribution.
;
; Neither the name of Texas Instruments Incorporated nor the names of
; its contributors may be used to endorse or promote products derived
; from this software without specific prior written permission.
;
; THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
; "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
; LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
; A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
; OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
; SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
; LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
; DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
; THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
; (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
; OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
;
;     file:   pru0_main.asm
;
;     brief:
;
;
;    Version        Description                                Author
;     0.1         Created                                      Thomas Leyrer

;************************************* includes *************************************

   .include "icss_core_clock_macros.inc"

;macro used to precisely wait for (P1 > 1) cycles
nopx    .macro P1
    loop endloop?, P1 - 1
    NOP
endloop?:
    .endm

;macro to write 32 bit register using r2, r3
HW_WR_REG32  .macro address, data_32

    ldi32    r23, data_32
	ldi32    r24, address
	sbbo     &r23, r24, 0, 4
    .endm

; compile time settings for GPIO modes	
PRU_GPI          .set       0  ; 0 = system GPI, 1 = PRU GPI
PRU_GPO          .set       0   ; 0 = system GPO, 1 = PRU GPO


;CCS/makefile specific settings
    .retain     ; Required for building .out with assembly file
    .retainrefs ; Required for building .out with assembly file

  	.global     main
    .sect    ".text"


;********
;* MAIN *
;********

main:
    zero	&r0, 120

; disable task manager
    tsen 0
	
    m_set_icssg_1_core_clock_333MHz
	
 ; C28 for shared memory needs initialization through offset register
 .if $defined(PRU0)
    ldi     r2, 0x0100
 .else
    ldi     r2, 0x0110
 .endif
   sbco    &r2, c11, 0x28, 2

;************************************* padconfig *************************************
; unlock PADMMR config register
; partition 0
    ldi32    r2, 0x000f1008  ; LOCK0 KICK0 register
    ldi32    r3, 0x000f100c  ; LOCK0 KICK1 register
    ldi32    r4, 0x68EF3490  ; Kick 0
    ldi32    r5, 0xD172BC5A  ; kick 1

    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; partition 1
    ldi32    r2, 0x000f5008  ; LOCK1 KICK0 register
    ldi32    r3, 0x000f500c  ; LOCK1 KICK1 register

    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4
	
; pin-mux configuration - PRG0_PRU0_GPI1 - BP.32
; alternative system GPIO1_1
    ldi32    r2, 0x000F4164
 .if(PRU_GPI)
    ldi32    r3, 0x00040001
 .else 
    ldi32    r3, 0x00040007
 .endif      
    sbbo     &r3, r2, 0, 4
	
; dir register of GPIO1 bank 0 	
	ldi32    r2, 0x00601010
	ldi      r3, 0xffff
	sbbo     &r3.w0, r2, 0, 2

; pin-mux configuration - PRG0_PRU0_GPO0 - BP.33
    ldi32    r2, 0x000F4160
 .if(PRU_GPO)
    ldi32    r3, 0x00010000
 .else
    ldi32    r3, 0x00010007
 .endif
    sbbo     &r3, r2, 0, 4

 .if(PRU_GPO==0)
; dir register of GPIO1 bank 0
	ldi32    r2, 0x00601010
	ldi      r3, 0xfffe
	sbbo     &r3.w0, r2, 0, 2
 .endif

 	
; pre-load in_data register for GPIO1_1
    ldi32    r2, 0x00601000
    ldi      r4.b0, 0x01
	
;************************************* GPIO latency loop *************************************
; follow GPI pin in PRU mode and ststem mode
; r31 bit 1 maps to PRU0_GPI1
; r30 bit 0 maps to PRU0_GPO0
;
; system GPIO offsets to base address 0x00601000 
; 0x18 - set data
; 0x1C - clr data
; 0x20 - in_data

idle_loop:

; poll for rising edge
 .if(PRU_GPI)
   wbs     r31,  1
 .else
wait_high:
   lbbo    &r3,r2, 0x20 , 1
   qbbc    wait_high, r3.b0, 1
 .endif
; set GPO
 .if(PRU_GPO)
   set     r30, r30, 0
 .else
   sbbo    &r4.b0, r2, 0x18, 1
 .endif

 ; poll for falling edge
 .if(PRU_GPI)
   wbc     r31,  1
 .else
wait_low:
   lbbo    &r3,r2, 0x20 , 1
   qbbs    wait_low, r3.b0, 1
 .endif
; clear GPO
 .if(PRU_GPO)
   clr     r30, r30, 0
 .else
   sbbo    &r4.b0, r2, 0x1c, 1
 .endif
   qba     idle_loop	


   halt

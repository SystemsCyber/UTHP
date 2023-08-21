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

TM_YIELD_XID     .set 		252
BANK1_ID         .set       10



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

; pin-mux configuration - PRG1_PRU0_GPO5 - BP.46
    ldi32    r2, 0x000F40CC
    ldi32    r3, 0x00010000
    sbbo     &r3, r2, 0, 4

 .if(0)
; ************************************ INTC config ***********************************
; internal event 16 to channel 7 and host 7 (task manager)
; internal event 17 to channel 8 and host 8 (task manager)

; first configure type for event 16/17 INTC_TYPE_REG4 - should be level triggered
    ldi32    r2,0x00020D80
	ldi32    r3,0x00000000   ; bit 16 and 17 maps to events 16 and 17, edge triggered when set
    sbbo     &r3, r2, 0, 4
	
; map event 16/17 to channel 7/8 which is routed to task manager 
    ldi32    r2,0x00020410   ; CH_MAP_REG4 has event 16 and 17 mapping
	ldi32    r3,0x00000807   ;
    sbbo     &r3, r2, 0, 4

; enable event 16 / 17
    ldi32    r2,0x00020300   ; INTC_ENABLE_REG0
	ldi32    r3,0x00030000   ; bit 16 and 17 maps to event 16 , 17
    sbbo     &r3, r2, 0, 4
	
; enable event_status  16/17 	
    ldi32    r2,0x00020280   ; INTC_ENABLE_STATUS_REG4
	ldi32    r3,0x00030000   ; bit 16 and 17
    sbbo     &r3, r2, 0, 4

; map channel to host interrupt. Channel 7 to host 7    
    ldi32    r2,0x00020804   ; HINT_MAP_REG1 has channel 7 
	ldi32    r3,0x07000000     
    sbbo     &r3, r2, 0, 4

; map channel to host interrupt. Channel 8 to host 8    
    ldi32    r2,0x00020808   ; HINT_MAP_REG2 has channel 5 and 6
	ldi32    r3,0x00000008
    sbbo     &r3, r2, 0, 4
	

; enable HINT channel 7/8
    ldi32    r2,0x00021500   ; ENABLE_HINT_REG0
	ldi32    r3,0x00000180   ; bit 7 and 8
    sbbo     &r3, r2, 0, 4
	
; global engable for all HINT
    ldi32    r2,0x00020010   ; GLOBAL_ENABLE_HINT_REG
	ldi32    r3,0x00000001   ; bit 0 enables all registers   
    sbbo     &r3, r2, 0, 4	
  .endif	
	
idle_loop:
; generate a 1 MHz sqaure wave on ICSS_G1_PRU0_GPO_5 (BP.46)
; for exact 1.00 Mhz use different PRU clock (300 MHz) or IEP_SYNC output
   set     r30, r30, 5
;   ldi     r31.b0, 0x20      ; pru_mst_intr[0]
;  165 * 3 ns = 495 ns
   nopx    166
   nopx    166
   clr     r30, r30, 5
;   ldi     r31.b0, 0x21      ; pru_mst_intr[1]
   nopx    166
   nopx    166
   qba     idle_loop	


    halt

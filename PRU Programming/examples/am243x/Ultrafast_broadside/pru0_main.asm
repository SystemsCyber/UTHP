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
;     file:   main.asm
;
;     brief:  PRU broadside widget
;
;
;    Version        Description                                Author
;     0.1         Created                                      Thomas Leyrer

;************************************* includes *************************************

; includes from \icss-g-industrial-fw\pru_fw_common
;    .include "pru_constant_defines.h"
;    .include "icss_iep_regs.inc"

;    .include "icss_intc_regs.h"

;************************************* macros *************************************


; global memory address
MS_RAM_BASE .set    0x70000000   ; 2 MB on-chip RAM optimized read latency from ICSS_G
MSRAM_BK0   .set    0x70000000   ; MS RAM is organized in 8 * 256kB, this is 1st block
MSRAM_BK1   .set    0x70040000   ; MS RAM is organized in 8 * 256kB, this is 2nd block
MSRAM_BK2   .set    0x70080000   ; 
; ....
DDR_RAM     .set    0x80000000   ; DDR memory
R5FSS0_ATCM .set    0x78000000   ; 64 kB TCM of firt ARM R5FSS0_ATCM
R5FSS0_BTCM .set    0x78000000   ; 64 kB TCM of firt ARM R5FSS0_ATCM
R5FSS1_ATCM .set    0x78000000   ; 64 kB TCM of firt ARM R5FSS0_ATCM    
R5FSS1_BTCM .set    0x78000000   ; 64 kB TCM of firt ARM R5FSS0_ATCM    


   .asg r18    , xfr2vbus_addr
   .asg r19    , xfr2vbus_addr_high

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

; fill r0-r29 with incremental bytes from 0 to 119
; loop instruction saves two instructions per iteration
; pointer increment and eof loop check
; each iteration takes two cycles instead of 3 cycles.
    ldi     r1.b0, 120
	loop    endloop, r1.b0
	mvib    *--r1.b0, r1.b0
endloop:
; restore value in r1.b0 which is the pointer
    ldi     r1.b0, 4   

; perform bytes swaps with different length
    xin    160, &r0, 4
    xin    160, &r1, 120-4
    xin    160, &r0.b3, 2

; perform 4_8 register swap
    xin    161, &r2, 8*4
    xin    161, &r2, 8*4

; perform 4_16 register swap
    xin    162, &r2, 16*4
    xin    162, &r2, 16*4

; init xfr2vbus write dma
   ldi32 xfr2vbus_addr, MSRAM_BK0 ; write to MSRAM
   ldi   xfr2vbus_addr_high, 0    ; 48 bit address extension

; execute xfr2vbus_write - 64 byte non blocking write operation
   xout  0x62, &r2, 68  

; same memory transfer with sbco instruction takes 17 cycles
   sbco  &r2, c16, 0x40, 64
   nop
   
   halt
   

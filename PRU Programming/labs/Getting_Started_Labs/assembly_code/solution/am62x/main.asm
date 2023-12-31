; Copyright (C) 2018-2021 Texas Instruments Incorporated - http://www.ti.com/
;
; Redistribution and use in source and binary forms, with or without
; modification, are permitted provided that the following conditions
; are met:
;
;        * Redistributions of source code must retain the above copyright
;          notice, this list of conditions and the following disclaimer.
;
;        * Redistributions in binary form must reproduce the above copyright
;          notice, this list of conditions and the following disclaimer in the
;          documentation and/or other materials provided with the
;          distribution.
;
;        * Neither the name of Texas Instruments Incorporated nor the names of
;          its contributors may be used to endorse or promote products derived
;          from this software without specific prior written permission.
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
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;*****************************************************************************
;  Define x, y, z values. Define storage registers
;*****************************************************************************

; TODO: define y and z
x				.set	1
y				.set	2
z				.set    0

; TODO: define y_register and z_register
x_register			.set	r20
y_register			.set	r21
z_register			.set	r22

;*****************************************************************************
;                                  Main Loop
;*****************************************************************************
	.sect	".text:main"
	.clink
	.global	||main||

||main||:

	; TODO: clear y_register and z_register
	zero		&x_register, 4		; Clear register 20
	zero		&y_register, 4		; Clear register 21
	zero		&z_register, 4		; Clear register 22

while_true:

	; TODO: load y value into y_register
	ldi		x_register, x		; load x value into register r20
	ldi		y_register, y		; load y value into register r21

	; TODO: add x_register and y_register. Store the result in z_register
	add		z_register, x_register, y_register


	; jump to continue refreshing z_register value
	jmp		while_true

	; the jump prevents us from getting to halt
	halt					; Halt PRU execution

;*****************************************************************************
;                                     END
;*****************************************************************************

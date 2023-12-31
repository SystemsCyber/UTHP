/*
 * Copyright (C) 2018-2021 Texas Instruments Incorporated - http://www.ti.com/
 *
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *
 *  * Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the
 *    distribution.
 *
 *  * Neither the name of Texas Instruments Incorporated nor the names of
 *    its contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <stdint.h>

/* TODO: define c */
/* a, b, and c are stored in a defined location in PRU memory */
#define a  (*((volatile unsigned int *)0x110))
#define b  (*((volatile unsigned int *)0x114))
#define c  (*((volatile unsigned int *)0x118))

/* Declaration of the external assembly function */
uint32_t assm_add(uint32_t arg1, uint32_t arg2);

/*
 * main.c
 */
void main(void)
{
    /* TODO: define y & z */
    /* The compiler decides where to store x, y, and z */
    uint32_t x = 1;
    uint32_t y = 2;
    uint32_t z = 0;

    a = 1;
    b = 2;

    while(1) {
        /*
         * TODO: use the assembly function to add x and y, then
         * store the sum in z
         */
        z = assm_add(x, y);

        /*
         * TODO: use the assembly function to add a and b, then
         * store the sum in memory location c
         */
        c = assm_add(a, b);
    }

    /* This program will not reach __halt because of the while loop */
    __halt();
}

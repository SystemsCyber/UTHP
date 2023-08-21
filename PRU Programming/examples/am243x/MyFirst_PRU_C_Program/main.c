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

/* a, b, and c are stored in a defined location in PRU data memory */
#define a  (*((volatile unsigned int *)0x110))
#define b  (*((volatile unsigned int *)0x114))
#define c  (*((volatile unsigned int *)0x118))

int max(int num1, int num2);


/*
 * main.c
 */
void main(void)
{

    /* The compiler decides where to store x, y, and z */
    uint32_t x = 1;
    uint32_t y = 2;
    uint32_t z = 0;

    a = 1;
    b = 2;

    while(1) {

        z = x + y;

        /*
         * store the sum of the numbers at memory locations a and
         * b in memory location c
         */
        c = a + b;

        /* get max from two numbers using C function call */
        c = max(a,b);

        /* get max from two numbers using inline assembly */
        __asm("   max r6, r4, r5");

    }

    /* This program will not reach __halt because of the while loop */
    __halt();
}


int max(int num1, int num2) {

    /*
     * Function input arguments are stored in R14-R29.
     * So the 32 bit value in arg1 is stored in R14, and the 32 bit value in
     * arg2 is stored in R15.
     *
     * For more details about how function arguments
     * are stored in registers, reference the document "PRU Optimizing C/C+
     * Compiler User's Guide", section "Function Structure and Calling
     * Conventions"
     */

   int max_value;

   if (num1 > num2)
      max_value = num1;
   else
      max_value = num2;

   /*
    * Remember return register is R14
    */
   return max_value;
}

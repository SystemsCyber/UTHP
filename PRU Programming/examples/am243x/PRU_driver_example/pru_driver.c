/*
 *  Copyright (C) 2021 Texas Instruments Incorporated
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *    Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *
 *    Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the
 *    distribution.
 *
 *    Neither the name of Texas Instruments Incorporated nor the names of
 *    its contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 *  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 *  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 *  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 *  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 *  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <stdio.h>
#include <kernel/dpl/DebugP.h>
#include "ti_drivers_config.h"
#include "ti_drivers_open_close.h"
#include "ti_board_open_close.h"
#include "lab_instr1_firmware.h"

extern PRUICSS_Config gPruicssConfig[2];
static void PRU_IsrFxn(void);

/** \brief Global Structure pointer holding PRUSS1 memory Map. */
PRUICSS_Handle gPruIcss0Handle;

static void *gPru_cfg, *gPru_ctrl;
void *gPru_dramx;
HwiP_Object         gPRUHwiObject;

#define CTR_EN (1 << 3)

/*
 * This is an empty project provided for all cores present in the device.
 * User can use this project to start their application by adding more SysConfig modules.
 *
 * This application does driver and board init and just prints the pass string on the console.
 * In case of the main core, the print is redirected to the UART console.
 * For all other cores, CCS prints are used.
 */

void generic_pruss_init()
{
    HwiP_Params     hwiPrms;
    int32_t         retVal;
    uint32_t        intrNum;

// mapping of PRU INTC host interrupts to ARM R5F interrupt
//   host0 = 120
//   ...
//   host7 = 127
    intrNum          = 253;

    gPruIcss0Handle = PRUICSS_open(CONFIG_PRU_ICSS0);

    PRUICSS_disableCore(gPruIcss0Handle, PRUICSS_PRU0);

    /* clear ICSS0 PRU data RAM */
    gPru_dramx = (void *)((((PRUICSS_HwAttrs *)(gPruIcss0Handle->hwAttrs))->baseAddr) + PRUICSS_DATARAM(PRUICSS_PRU0));
    memset(gPru_dramx, 0, (4 * 1024));

    gPru_cfg = (void *)(((PRUICSS_HwAttrs *)(gPruIcss0Handle->hwAttrs))->cfgRegBase);

    /* taken from sysconfig in file  ti_drivers_config.c */
    PRUICSS_intcInit(gPruIcss0Handle, &icss0_intc_initdata);

    /* Register PRU interrupt */
    HwiP_Params_init(&hwiPrms);
    hwiPrms.intNum   = intrNum;
    hwiPrms.callback = (void *) &PRU_IsrFxn;
    retVal = HwiP_construct(&gPRUHwiObject, &hwiPrms);

    /* configure C28 to PRU_ICSS_CTRL and C29 to EDMA + 0x1000 */
    /*6.4.14.1.1 ICSSG_PRU_CONTROL RegisterPRU_ICSSG0_PR1_PDSP0_IRAM 00B0 2400h*/
    PRUICSS_setConstantTblEntry(gPruIcss0Handle, PRUICSS_PRU0, PRUICSS_CONST_TBL_ENTRY_C28, 0x0240);
    /*IEP1 base */
    PRUICSS_setConstantTblEntry(gPruIcss0Handle, PRUICSS_PRU0, PRUICSS_CONST_TBL_ENTRY_C29, 0x0002F000);

    /* enable cycle counter */
    gPru_ctrl =  (void *)((((PRUICSS_HwAttrs *)(gPruIcss0Handle->hwAttrs))->baseAddr) + CSL_ICSS_G_PR1_PDSP1_IRAM_REGS_BASE);

    HW_WR_REG32(gPru_ctrl, CTR_EN);


    PRUICSS_writeMemory(gPruIcss0Handle, PRUICSS_IRAM_PRU(PRUICSS_PRU0),
                     0, (uint32_t *) lab_instr1_image_0,
                     sizeof(lab_instr1_image_0));

    PRUICSS_resetCore(gPruIcss0Handle, PRUICSS_PRU0);

    /*Run firmware*/
    PRUICSS_enableCore(gPruIcss0Handle, PRUICSS_PRU0);

}

//  PRU instruction causing the interrupt -
//  ldi    r31, 0x20  ; interrupt 0 + enable (bit 5)
//
static void PRU_IsrFxn()
{
    int    status;


// clear EDIO28 -> mapped to HDSL channel 1 input (C1_I)
//  HW_WR_REG32((0X3002E310), (0x00000000));
    status = PRUICSS_clearEvent(gPruIcss0Handle, 16);  // 16 is PRU0 intr[0]

//  HW_WR_REG32((0x3002e310), (0x00000000));

}

void empty_main(void *args)
{
    /* Open drivers to open the UART driver for console */
    Drivers_open();
    Board_driversOpen();

    /* open PRU driver for generic functions - download fw, set INT, start core, . */
    generic_pruss_init();

    DebugP_log("All tests have passed!!\r\n");

    while (1);

    Board_driversClose();
    Drivers_close();
}


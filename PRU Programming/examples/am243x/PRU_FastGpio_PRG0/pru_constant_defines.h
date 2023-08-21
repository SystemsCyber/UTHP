;************************************************************************************
;**+------------------------------------------------------------------------------+**
;**|                              ******                                          |**
;**|                              ******     o                                    |**
;**|                              *******__////__****                             |**
;**|                              ***** /_ //___/ ***                             |**
;**|                           ********* ////__ ******                            |**
;**|                             *******(_____/ ******                            |**
;**|                                 **********                                   |**
;**|                                   ******                                     |**
;**|                                      ***                                     |**
;**|                                                                              |**
;**|            Copyright (c) 2017 Texas Instruments Incorporated                 |**
;**|                           ALL RIGHTS RESERVED                                |**
;**|                                                                              |**
;**|    Permission is hereby granted to licensees of Texas Instruments            |**
;**|    Incorporated (TI) products to use this computer program for the sole      |**
;**|    purpose of implementing a licensee product based on TI products.          |**
;**|    No other rights to reproduce, use, or disseminate this computer           |**
;**|    program, whether in part or in whole, are granted.                        |**
;**|                                                                              |**
;**|    TI makes no representation or warranties with respect to the              |**
;**|    performance of this computer program, and specifically disclaims          |**
;**|    any responsibility for any damages, special or consequential,             |**
;**|    connected with the use of this program.                                   |**
;**|                                                                              |**
;**+------------------------------------------------------------------------------+**
;************************************************************************************
; file:     pru_constant_defines.h
;
; brief:    Constant defines
;           Includes:
;           1.
;

    .if !$isdefed("____pru_constant_defines_h")
____pru_constant_defines_h   .set    1


;--------------------------------------------------------------------------;
;   Constants: R31 Command Interface Bits
;
;   R31_CMD_TX_CRC_ERR_bit - Generate TX CRC Error - HW corrupts CRC
;   R31_CMD_TX_RESET_bit  - Reset TXL1 and TXL2 (if exists/enabled) FIFOs
;   R31_CMD_TX_EOF_CMD_MASK_bit - Issue TX_EOF to complte frame send
;   R31_CMD_TX_ERROR_NIBBLE_bit - Issue odd nibble post CRC to force alignment error
;   R31_CMD_TX_CRC_HIGH_bit - Push MSW for CRC to TX FIFO
;   R31_CMD_TX_CRC_LOW_bit - Push LSW for CRC to TX FIFO
;   R31_CMD_TX_PUSH_16_bit - Push 16-bit of Data (R30.w0) to TXL1 FIFO
;   R31_CMD_TX_PUSH_8_bit - Push 8-bit of Data (R30.b0) to TXL1 FIFO
;   R31_CMD_RX_ERROR_CLR_bit - Clear RX_ERROR bit in R31
;   R31_CMD_RX_EOF_CLR_bit - Clear RX_EOF indication in R31
;   R31_CMD_RX_SFD_CLR_bit - Clear RX_SFD indication in R31
;   R31_CMD_RX_RESET_bit - Reset RXL1 and RXL2 (if enabled) FIFOs
;   R31_CMD_RX_POP_16_bit - Pop 16-bits from RXL1 FIFO to R31 (Used for on the fly processing)
;   R31_CMD_RX_POP_8_bit - Pop 8-bits from RXL1 FIFO to R31(Used for on the fly processing)
;
;--------------------------------------------------------------------------;
R31_CMD_TX_CRC_ERR_bit            .set    31
R31_CMD_TX_RESET_bit              .set    30
R31_CMD_TX_EOF_CMD_MASK_bit       .set    29
R31_CMD_TX_ERROR_NIBBLE_bit       .set    28
R31_CMD_TX_CRC_HIGH_bit           .set    27
R31_CMD_TX_CRC_LOW_bit            .set    26
R31_CMD_TX_PUSH_16_bit            .set    25
R31_CMD_TX_PUSH_8_bit             .set    24
R31_CMD_RX_ERROR_CLR_bit          .set    23
R31_CMD_RX_EOF_CLR_bit            .set    22
R31_CMD_RX_SFD_CLR_bit            .set    21
R31_CMD_RX_SOF_CLR_bit            .set    20
R31_CMD_RESERVED_bit              .set    19
R31_CMD_RX_RESET_bit              .set    18
R31_CMD_RX_POP_16_bit             .set    17
R31_CMD_RX_POP_8_bit              .set    16

;--------------------------------------------------------------------------;
;   Constants: R31 Command Masks
;
;   R31_CMD_TX_CRC_ERR_mask - Generate TX CRC Error - HW corrupts CRC
;   R31_CMD_RESET_TXFIFO_mask  - Reset TXL1 and TXL2 (if exists/enabled) FIFOs
;   R31_CMD_TX_EOF_mask - Issue TX_EOF to complte frame send
;   R31_CMD_PUSH_ERR_NIBBLE_mask - Issue odd nibble post CRC to force alignment error
;   R31_CMD_PUSH_CRC_MSWORD_mask - Push MSW for CRC to TX FIFO
;   R31_CMD_PUSH_CRC_LSWORD_mask - Push LSW for CRC to TX FIFO
;   R31_CMD_PUSH_CRC_mask - Push CRC to TX FIFO
;   R31_CMD_PUSH_WORD_mask - Push 16-bit of Data (R30.w0) to TXL1 FIFO
;   R31_CMD_PUSH_BYTE_mask - Push 8-bit of Data (R30.b0) to TXL1 FIFO
;   R31_CMD_RX_ERROR_CLR_mask - Clear RX_ERROR bit in R31
;   R31_CMD_RX_EOF_CLEAR_mask - Clear RX_EOF indication in R31
;   R31_CMD_RX_SFD_CLR_mask - Clear RX_SFD indication in R31
;   R31_CMD_RESET_RXFIFO_mask - Reset RXL1 and RXL2 (if enabled) FIFOs
;   R31_CMD_POP_WORD_mask - Pop 16-bits from RXL1 FIFO to R31 (Used for on the fly processing)
;   R31_CMD_POP_BYTE_mask - Pop 8-bits from RXL1 FIFO to R31(Used for on the fly processing)
;
;--------------------------------------------------------------------------;
R31_CMD_TX_CRC_ERR_mask         .set    0x8000
R31_CMD_RESET_TXFIFO_mask       .set    0x4000
R31_CMD_TX_EOF_mask             .set    0x2000
R31_CMD_PUSH_ERR_NIBBLE_mask    .set    0x1000
R31_CMD_PUSH_CRC_MSWORD_mask    .set    0x0800
R31_CMD_PUSH_CRC_LSWORD_mask    .set    0x0400
R31_CMD_PUSH_CRC_mask           .set    0x0C00
R31_CMD_PUSH_WORD_mask          .set    0x0200
R31_CMD_PUSH_BYTE_mask          .set    0x0100
R31_CMD_RX_ERROR_CLR_mask       .set    0x0080
R31_CMD_RX_EOF_CLEAR_mask       .set    0x0040
R31_CMD_RX_SFD_CLR_mask         .set    0x0020
R31_CMD_RX_SOF_CLR_mask         .set    0x0010
R31_CMD_RESET_RXFIFO_mask       .set    0x0004
R31_CMD_POP_WORD_mask           .set    0x0002
R31_CMD_POP_BYTE_mask           .set    0x0001

R31_CMD_PUSH_N_POP_BYTE_mask    .set    (R31_CMD_POP_BYTE_mask | R31_CMD_PUSH_BYTE_mask)
R31_CMD_PUSH_N_POP_WORD_mask    .set    (R31_CMD_POP_WORD_mask | R31_CMD_PUSH_WORD_mask)
R31_CMD_PUSH_CRC_N_TX_EOF_mask  .set    (R31_CMD_TX_EOF_mask | R31_CMD_PUSH_CRC_MSWORD_mask | R31_CMD_PUSH_CRC_LSWORD_mask)

;--------------------------------------------------------------------------;
;   Constants: R31 Receive Interface Bits
;
;   R31_RCV_RX_MIN_FRM_CNT_ERR_bit  - Short (than configured) frame error detected
;   R31_RCV_RX_MAX_FRM_CNT_ERR_bit  - Long (than configured) frame error detected
;   R31_RCV_RX_EOF_ERROR_bit - RX_ERROR and/or RX_EOF detected
;   R31_RCV_RX_MAX_PRE_CNT_ERROR_bit - Max Preamble Error (Longer than configured)
;   R31_RCV_RX_ERR_bit  - MII RX ERR detected
;   R31_RCV_ERROR_CRC_bit - CRC error detected in received frame
;   R31_RCV_ERROR_NIBBLE_bit - Odd nibble/alignement error detected in received frame
;   R31_RCV_RX_SOF_bit - RX SOF detected (RX_DV asserted at MII interface)
;   R31_RCV_RX_SFD_bit  - RX SFD detected
;   R31_RCV_RX_EOF_bit  - RX EOF detected (RX_DV de-asserted at MII interface)
;   R31_RCV_RX_ERROR_bit - RX_ERROR detected in received frame
;   R31_RCV_WORD_RDY_bit - All 4 nibbles in R31 is valid
;   R31_RCV_BYTE_RDY_bit - Lower 2 nibbles in R31 is valid
;   R31_RCV_DATA_RDY_bit  - R31 is valid, cleared on pop, set for WORD/BYTE (obsolete)
;   R31_RCV_TX_EOF_bit  - TX_EN de-asserted at MII interface
;
;--------------------------------------------------------------------------;
R31_RCV_RESERVED1_bit                 .set    31
R31_RCV_RESERVED0_bit                 .set    30
R31_RCV_RX_MIN_FRM_CNT_ERR_bit        .set    29
R31_RCV_RX_MAX_FRM_CNT_ERR_bit        .set    28
R31_RCV_RX_EOF_ERROR_bit              .set    27
R31_RCV_RX_MAX_PRE_CNT_ERROR_bit      .set    26
R31_RCV_RX_ERR_bit                    .set    25
R31_RCV_ERROR_CRC_bit                 .set    24
R31_RCV_ERROR_NIBBLE_bit              .set    23
R31_RCV_RX_SOF_bit                    .set    22
R31_RCV_RX_SFD_bit                    .set    21
R31_RCV_RX_EOF_bit                    .set    20
R31_RCV_RX_ERROR_bit                  .set    19
R31_RCV_WORD_RDY_bit                  .set    18
R31_RCV_BYTE_RDY_bit                  .set    17
R31_RCV_DATA_RDY_bit                  .set    16
R31_RCV_TX_EOF_bit                    .set    16

;--------------------------------------------------------------------------;
;   Constants: Global Constant Table Entries
;
;   ICSS_INTC_CONST  - ICSS Interrupt Controller Registers Base Address
;   ICSS_IEP1_0_CONST - ICSS IEP1 offset
;   ICSS_IEP1_1_CONST - ICSS IEP1 + 0x100 offset for optimal access from firmware
;   ICSS_ECAP_CONST  - ICSS Enhanced Capture Registers Base Address
;   ICSS_CFG_CONST - ICSS CFG Registers Base Address
;   ICSS_CFG_1_CONST - ICSS ICFG + 0x100 offset for optimal access from firmware
;   ICSS_INTC_2_CONST - ICSS INTC + 0x200 offset for optimal access from firmware 
;   ICSS_UART_CONST - ICSS UART Registers Base Address
;   ICSS_IEP0_1_CONST - ICSS IEP0 + 0x100 offset for optimal access from firmware
;   ICSS_G_CFG_CONST - ICSS_G CFG Registers Base Address
;   ICSS_TM_CFG_CONST - ICSS Task Manager Config Base Address for PRU0/1 and RTU0/1
;   ICSS_PRU_CTRL_CONST - ICSS PRU Control Registers Base Address for PRU/RTU/0/1
;   ICSS_PA_STAT_QRAM_CONST - ICSS PASTAT Query RAM Base Address
;   ICSS_PA_STAT_CRAM_CONST - ICSS PASTAT Clear on Read RAM Base Address
;   ICSS_PROTECT_CONST - ICSS Protect Registers Base Address
;   ICSS_RAT_REGION0_CONST - ICSS RAT REGION0 (Map SoC address to 0x6000_0000 in RAT)
;   ICSS_RAT_REGION1_CONST - ICSS RAT REGION1 (Map SoC address to 0x7000_0000 in RAT)
;   ICSS_RAT_REGION2_CONST - ICSS RAT REGION2 (Map SoC address to 0x8000_0000 in RAT)
;   ICSS_RAT_REGION3_CONST - ICSS RAT REGION3 (Map SoC address to 0x9000_0000 in RAT)
;   ICSS_RAT_REGION4_CONST - ICSS RAT REGION4 (Map SoC address to 0xA000_0000 in RAT)
;   ICSS_RAT_REGION5_CONST - ICSS RAT REGION5 (Map SoC address to 0xB000_0000 in RAT)
;   ICSS_MDIO_CONST  - ICSS MII-MDIO Registers Base Address
;   ICSS_RAT_CONST - ICSS RAT Config Registers Base Address
;   ICSS_RAT_REGION6_CONST - ICSS RAT REGION6 (Map SoC address to 0xC000_0000 in RAT)
;   ICSS_DMEM0_CONST  - ICSS Data Memory 0 Base Address
;   ICSS_DMEM1_CONST  - ICSS Data Memory 1 Base Address
;   ICSS_IEP_CONST  - ICSS Industrial Ethernet Peripheral Registers Base Address
;   ICSS_MII_RT_CONST  - ICSS Real-time MII Registers Base Address
;   ICSS_SMEM_CONST  - ICSS Shared Memory Base Address
;   ICSS_RAT_REGION7_CONST - ICSS RAT REGION7 (Map SoC address to 0xD000_0000 in RAT)
;   ICSS_RAT_REGION8_CONST - ICSS RAT REGION8 (Map SoC address to 0xE000_0000 in RAT)
;   ICSS_RAT_REGION9_CONST - ICSS RAT REGION9 (Map SoC address to 0xF000_0000 in RAT)
;--------------------------------------------------------------------------;

;From ICSSG Functional Spec, section 5.2.4
;Entry	Region Pointed To	value
;0	Local INTC	0x0002_0000
;1	IEP1 (local)	0x0002_F000
;2	IEP1_0x100(local)	0x0002_F100
;3	eCAP(local)	0x0003_0000
;4	ICSS CFG(local)	0x0002_6000
;5	ICSS CFG_0x100 (local)	0x0002_6100
;6	INTC_0x200 (local)	0x0002_0200
;7	UART 0(local)	0x0002_8000
;8	IEP0_0x100(local)	0x0002_E100
;9	ICSS_G_CFG (local)	0x0003_3000
;10	TM_CFG_PRU/RTU0/1 (local)	0x0002_A000 PRU0 0x0002_A100 RTU0 0x0002_A200 PRU1 0x0002_A300 RTU1
;11	PRU/RTU/0/1 control (local)	0x0002_2000 PRU0 0x0002_4000 PRU1 0x0002_3000 RTU0 0x0002_3800 RTU1
;12	PA_STAT_QRAM(local)	0x0002_7000
;13	PA_STAT_CRAM(local)	0x0002_C000
;14	ICSS_Protect(local)	0x0002_4800
;15	Timer Manager (NAVSS) – RAT0/1	0x6000_0000
;16	RA (NAVSS) – RAT0/1	0x7000_0000
;17	IA (NAVSS) – RAT0/1	0x8000_0000
;18	GPMC – RAT0/1	0x9000_0000
;19	PCIE – RAT0/1	0xA000_0000
;20	UDMA-P – RAT0/1	0xB000_0000
;21	MDIO(local)	0x0003_2400
;22	RAT slice 0/1 (local)	0x0000_8000 PRU0/RTU0 0x0000_9000 PRU1/RTU1
;23	ADC - RAT0/1	0xC000_0000
;24	PRU0/1 Local Data	{20’h0000_0,c24_blk_index[3:0],8’h00}
;25	PRU1/0 Local Data	{20’h0000_2,c25_blk_index[3:0],8’h00}
;26	IEP(local)	{20’h0002_E,c26_blk_index[3:0],8’h00}
;27	MII_RT (local)/SGMII0/1_CFG	{20’h0003_2,c27_blk_index[3:0],8’h00}
;28	RAM 1_0(local)	{8'h00,ct_prt0[15:0],8'h00}
;29	DDR - RAT0/1	{8’hD0,ct_prt1[15:0],8'h00}
;30	MSMC - RAT0/1	{8’hE0,ct_prt2[15:0],8'h00}
;31	R5 RAM - RAT0/1	{8’hF0,ct_prt3[15:0],8'h00}

    .asg c0,  ICSS_INTC_CONST
    .asg c1,  ICSS_IEP1_0_CONST
    .asg c2,  ICSS_IEP1_1_CONST ; IEP1 + 0x100 offset
    .asg c3,  ICSS_ECAP_CONST
    .asg c4,  ICSS_CFG_CONST
    .asg c5,  ICSS_CFG_1_CONST ; CFG + 0x100 offset
    .asg c6,  ICSS_INTC_2_CONST ; INTC + 0x200 offset
    .asg c7,  ICSS_UART_CONST
    .asg c8,  ICSS_IEP0_1_CONST ; IEP0 + 0x100 offset
    .asg c9,  ICSS_G_CFG_CONST
    .asg c10, ICSS_TM_CFG_CONST
    .asg c11, ICSS_PRU_CTRL_CONST
    .asg c12, ICSS_PA_STAT_QRAM_CONST
    .asg c13, ICSS_PA_STAT_CRAM_CONST
    .asg c14, ICSS_PROTECT_CONST
    .asg c15, ICSS_RAT_REGION0_CONST ;0x6000_0000
    .asg c16, ICSS_RAT_REGION1_CONST ;0x7000_0000
    .asg c17, ICSS_RAT_REGION2_CONST ;0x8000_0000
    .asg c18, ICSS_RAT_REGION3_CONST ;0x9000_0000
    .asg c19, ICSS_RAT_REGION4_CONST ;0xA000_0000
    .asg c20, ICSS_RAT_REGION5_CONST ;0xB000_0000
    .asg c21, ICSS_MDIO_CONST
    .asg c22, ICSS_RAT_CONST
    .asg c23, ICSS_RAT_REGION6_CONST ;0xC000_0000
    .asg c24, ICSS_DMEM0_CONST
    .asg c25, ICSS_DMEM1_CONST
    .asg c26, ICSS_IEP_CONST
    .asg c27, ICSS_MII_RT_CONST
    .asg c28, ICSS_SMEM_CONST
    .asg c29, ICSS_RAT_REGION7_CONST ;0xD000_0000
    .asg c30, ICSS_RAT_REGION8_CONST ;0xE000_0000
    .asg c31, ICSS_RAT_REGION9_CONST ;0xF000_0000

ICSS_MSMC_RAM_CONST .set ICSS_RAT_REGION8_CONST

    .if $isdefed("PRU0")
PRU_DMEM_ADDR       .set    ICSS_DMEM0_CONST
PRU_CROSS_DMEM      .set    ICSS_DMEM1_CONST
    .else ;PRU1
PRU_DMEM_ADDR       .set    ICSS_DMEM1_CONST
PRU_CROSS_DMEM      .set    ICSS_DMEM0_CONST
    .endif

BANK0_ID             .set   10

    .endif ; ____pru_constant_defines_h

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
; file:     icss_core_clock_macros.inc
;
; brief:    Constant defines
;           Includes:
;           1.

m_set_icssg_1_core_clock_333MHz   .macro
;************************************* clock config **********************************
; core clock options:
; ICSSG0_CLKMUX_SEL: bit 0 = 1 PLL0, bit 0 = 0 PLL2 
; MAIN_PLL0_HSDIV9: 2 (333 MHz), 3 (250 MHz)
; MAIN_PLL2_HSDIV2: 5 (300 MHz), 7 (225 MHz)
;

; configure ICSS clocks
; unlock CTRLMMR config register
; partition 2
    ldi32    r2, 0x43009008  ; LOCK0 KICK0 register
    ldi32    r3, 0x4300900c  ; LOCK0 KICK1 register
    ldi32    r4, 0x68EF3490  ; kick 0
    ldi32    r5, 0xD172BC5A  ; kick 1
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; ICSS_Gx_CLKMUX_SEL:	
; 1h - MAIN_PLL0_HSDIV9_CLKOUT,
	ldi32    r2, 0x43008044
    ldi32	 r3, 0x00010001
    sbbo     &r3, r2, 0, 4

 .if(0)	
; run iep_clk with core clock	
	ldi32    r2, 0x00026030
    ldi32	 r3, 0x00000001
    sbbo     &r3, r2, 0, 4
 .endif

; unlock PLL0 ctrl register
    ldi32    r2, 0x00680010  ; LOCK0 KICK0 register
    ldi32    r3, 0x00680014  ; LOCK0 KICK1 register
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; set MAIN_PLL0_HSDIV9 to 2 for core_clock =333MHz (3 for 250 MHz)
	ldi      r2.b0, 2
	ldi32    r3, 0x006800a4
	sbbo     &r2, r3, 0, 1

	
; unlock PLL2 ctrl register
    ldi32    r2, 0x00682010  ; LOCK0 KICK0 register
    ldi32    r3, 0x00682014  ; LOCK0 KICK1 register
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; set core clock MAIN_PLL2_HSDIV0 to 5 for 300 MHz (7 for 225 MHz, 5 for 333 MHz)
    ldi      r2.b0, 5
    ldi32    r3, 0x00682080
    sbbo     &r2, r3, 0, 1

    .endm

m_set_icssg_0_core_clock_250MHz   .macro
;************************************* clock config **********************************
; core clock options:
; ICSSG0_CLKMUX_SEL: bit 0 = 1 PLL0, bit 0 = 0 PLL2 
; MAIN_PLL0_HSDIV9: 2 (333 MHz), 3 (250 MHz)
; MAIN_PLL2_HSDIV2: 5 (300 MHz), 7 (225 MHz)
;

; configure ICSS clocks
; unlock CTRLMMR config register
; partition 2
    ldi32    r2, 0x43009008  ; LOCK0 KICK0 register
    ldi32    r3, 0x4300900c  ; LOCK0 KICK1 register
    ldi32    r4, 0x68EF3490  ; kick 0
    ldi32    r5, 0xD172BC5A  ; kick 1
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; ICSS_Gx_CLKMUX_SEL:	
; 1h - MAIN_PLL0_HSDIV9_CLKOUT,
	ldi32    r2, 0x43008040
    ldi32	 r3, 0x00010001
    sbbo     &r3, r2, 0, 4

 .if(0)	
; run iep_clk with core clock	
	ldi32    r2, 0x00026030
    ldi32	 r3, 0x00000001
    sbbo     &r3, r2, 0, 4
 .endif

; unlock PLL0 ctrl register
    ldi32    r2, 0x00680010  ; LOCK0 KICK0 register
    ldi32    r3, 0x00680014  ; LOCK0 KICK1 register
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; set MAIN_PLL0_HSDIV9 to 2 for core_clock =333MHz (3 for 250 MHz)
	ldi      r2.b0, 3
	ldi32    r3, 0x006800a4
	sbbo     &r2, r3, 0, 1

	
; unlock PLL2 ctrl register
    ldi32    r2, 0x00682010  ; LOCK0 KICK0 register
    ldi32    r3, 0x00682014  ; LOCK0 KICK1 register
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; set core clock MAIN_PLL2_HSDIV0 to 5 for 300 MHz (7 for 225 MHz, 5 for 300 MHz)
    ldi      r2.b0, 5
    ldi32    r3, 0x00682080
    sbbo     &r2, r3, 0, 1

    .endm
	
m_set_icssg_0_core_clock_300MHz   .macro
;************************************* clock config **********************************
; core clock options:
; ICSSG0_CLKMUX_SEL: bit 0 = 1 PLL0, bit 0 = 0 PLL2 
; MAIN_PLL0_HSDIV9: 2 (333 MHz), 3 (250 MHz)
; MAIN_PLL2_HSDIV2: 5 (300 MHz), 7 (225 MHz)
;

; configure ICSS clocks
; unlock CTRLMMR config register
; partition 2
    ldi32    r2, 0x43009008  ; LOCK0 KICK0 register
    ldi32    r3, 0x4300900c  ; LOCK0 KICK1 register
    ldi32    r4, 0x68EF3490  ; kick 0
    ldi32    r5, 0xD172BC5A  ; kick 1
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; ICSS_Gx_CLKMUX_SEL:	
; 1h - MAIN_PLL0_HSDIV9_CLKOUT,
	ldi32    r2, 0x43008040
    ldi32	 r3, 0x00010000
    sbbo     &r3, r2, 0, 4

 .if(0)	
; run iep_clk with core clock	
	ldi32    r2, 0x00026030
    ldi32	 r3, 0x00000001
    sbbo     &r3, r2, 0, 4
 .endif

; unlock PLL0 ctrl register
    ldi32    r2, 0x00680010  ; LOCK0 KICK0 register
    ldi32    r3, 0x00680014  ; LOCK0 KICK1 register
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; set MAIN_PLL0_HSDIV9 to 2 for core_clock =333MHz (3 for 250 MHz)
	ldi      r2.b0, 3
	ldi32    r3, 0x006800a4
	sbbo     &r2, r3, 0, 1

	
; unlock PLL2 ctrl register
    ldi32    r2, 0x00682010  ; LOCK0 KICK0 register
    ldi32    r3, 0x00682014  ; LOCK0 KICK1 register
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; set core clock MAIN_PLL2_HSDIV0 to 5 for 300 MHz (7 for 225 MHz, 5 for 300 MHz)
    ldi      r2.b0, 5
    ldi32    r3, 0x00682080
    sbbo     &r2, r3, 0, 1

    .endm
	
m_set_icssg_0_core_clock_225MHz   .macro
;************************************* clock config **********************************
; core clock options:
; ICSSG0_CLKMUX_SEL: bit 0 = 1 PLL0, bit 0 = 0 PLL2 
; MAIN_PLL0_HSDIV9: 2 (333 MHz), 3 (250 MHz)
; MAIN_PLL2_HSDIV2: 5 (300 MHz), 7 (225 MHz)
;

; configure ICSS clocks
; unlock CTRLMMR config register
; partition 2
    ldi32    r2, 0x43009008  ; LOCK0 KICK0 register
    ldi32    r3, 0x4300900c  ; LOCK0 KICK1 register
    ldi32    r4, 0x68EF3490  ; kick 0
    ldi32    r5, 0xD172BC5A  ; kick 1
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; ICSS_Gx_CLKMUX_SEL:	
; 1h - MAIN_PLL0_HSDIV9_CLKOUT,
	ldi32    r2, 0x43008040
    ldi32	 r3, 0x00010000
    sbbo     &r3, r2, 0, 4

 .if(0)	
; run iep_clk with core clock	
	ldi32    r2, 0x00026030
    ldi32	 r3, 0x00000001
    sbbo     &r3, r2, 0, 4
 .endif

; unlock PLL0 ctrl register
    ldi32    r2, 0x00680010  ; LOCK0 KICK0 register
    ldi32    r3, 0x00680014  ; LOCK0 KICK1 register
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; set MAIN_PLL0_HSDIV9 to 2 for core_clock =333MHz (3 for 250 MHz)
	ldi      r2.b0, 3
	ldi32    r3, 0x006800a4
	sbbo     &r2, r3, 0, 1

	
; unlock PLL2 ctrl register
    ldi32    r2, 0x00682010  ; LOCK0 KICK0 register
    ldi32    r3, 0x00682014  ; LOCK0 KICK1 register
    sbbo     &r4, r2, 0, 4
    sbbo     &r5, r3, 0, 4

; set core clock MAIN_PLL2_HSDIV0 to 7 for 225 MHz (7 for 225 MHz, 5 for 300 MHz)
    ldi      r2.b0, 7
    ldi32    r3, 0x00682080
    sbbo     &r2, r3, 0, 1
	
    .endm
	
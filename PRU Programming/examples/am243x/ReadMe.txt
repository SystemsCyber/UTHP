<<<<<<< HEAD
Programmable Real-time Unit (PRU) Software Support Package
------------------------------------------------------------
============================================================
	AM24x EXAMPLES
============================================================

DESCRIPTION

	This directory provides basic "building block" examples for the AM243x
	PRU_ICSSG cores. The concepts shown in these examples can be combined to
	create PRU_ICSSG applications.


HELP! THE ICSSG EXAMPLES ARE STRUCTURED DIFFERENTLY THAN THE ICSS EXAMPLES!

	Project naming convention:
	PRU_xxx is for PRU cores
	RTU_xxx is for RTU cores (note the different command linker file)
	TX_PRU_xxx is for Tx_PRU cores

	We build firmware for multiple ICSSG instances in the Makefile
	(e.g., PRU_RPMsg_Echo_Interrupt0/Makefile builds firmware for PRU0 in
	ICSSG0 and ICSSG1). You could also have a separate project for
	each PRU/RTU core in each ICSSG, but we decided that many projects in
	the PRU Software Support Package (PSSP) would get overwhelming.


WHAT EXAMPLES ARE INCLUDED?

	EXAMPLE
	---------

	Getting started labs with RTOS and Code Composer Studio

		MyFirst_PRU_Assembler_Program
		MyFirst_PRU_C_Program
		MyFirst_PRU_mixed_Program
		PRU_driver_example

	PRU_FastGpio_PRG0

	PRU_FastGpio_PRG1

	Ultrafast_broadside

ADDITIONAL RESOURCES

	For more information about the PRU, visit:

	PRU-ICSS/PRU_ICSSG docs	 - https://software-dl.ti.com/processor-sdk-linux/esd/AM64X/latest/exports/docs/linux/Foundational_Components_PRU_Subsystem.html
	AM24x TRM                - https://www.ti.com/lit/pdf/spruim2
	Support                  - http://e2e.ti.com

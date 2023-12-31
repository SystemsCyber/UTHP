Programmable Real-time Unit (PRU) Software Support Package
------------------------------------------------------------
============================================================
	J721E EXAMPLES
============================================================

DESCRIPTION

	This directory provides basic "building block" examples for the J721E
	PRU_ICSSG cores. The concepts shown in these examples can be combined to
	create PRU_ICSSG applications.


"NO SUPPORT" NOTICE

	At this point in time, TI does NOT support PRU development on J721E.
	That means that TI cannot support J721e PRU development questions on the
	e2e.ti.com forums. These j721e examples are being maintained so that
	community members who want to develop without TI support
	have basic tools for their development.


HELP! THE ICSSG EXAMPLES ARE STRUCTURED DIFFERENTLY THAN THE ICSS EXAMPLES!

	Project naming convention:
	PRU_xxx is for PRU cores
	RTU_xxx is for RTU cores (note the different command linker file)
	TX_PRU_xxx is for Tx_PRU cores

	We build firmware for multiple ICSSG instances in the Makefile
	(e.g., PRU_RPMsg_Echo_Interrupt0/Makefile builds firmware for PRU0 in
	ICSSG0, ICSSG1, and ICSSG2). You could also have a separate project for
	each PRU/RTU core in each ICSSG, but we decided that many projects in
	the PRU Software Support Package (PSSP) would get overwhelming.


WHAT EXAMPLES ARE INCLUDED?

	EXAMPLE
	---------
	PRU_Halt
	RTU_Halt
	TX_PRU_Halt
		Halt examples are basic empty ICSS/ICSSG projects.
		The core gets initialized, and then does nothing.

	PRU_RPMsg_Echo_Interrupt0
	PRU_RPMsg_Echo_Interrupt1
	RTU_RPMsg_Echo_Interrupt0
	RTU_RPMsg_Echo_Interrupt1
		RPMsg examples demonstrate the RemoteProc RPMsg protocol to
		communicate between the ARM and the PRU. RPMsg is not the best
		inter-processor communication method for every design, but it is
		useful for initial debugging and demonstrations.


ADDITIONAL RESOURCES

	For more information about the PRU, visit:

	PRU-ICSS/PRU_ICSSG docs	 - https://software-dl.ti.com/processor-sdk-linux/esd/AM64X/latest/exports/docs/linux/Foundational_Components_PRU_Subsystem.html
	J721E TRM                - https://www.ti.com/lit/zip/spruil1
	Support                  - http://e2e.ti.com

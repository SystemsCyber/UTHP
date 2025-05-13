# Ultimate Truck Hacking Platform Hardware Design

The hardware design has the following main components:


2. [BeagleBone Black](https://www.beagleboard.org/boards/beaglebone-black)
2. [Printed Circuit Board (UTHP PCB)](Hardware\UTHP PCB)
1. Enclosure: Hammond [1455Q1602BK](https://www.hammfg.com/electronics/small-case/extruded/1455)
3. [Banana Jack Breakout Board](Enclosure%20Design/banana%20jack%20board%20schematic.pdf)
4. [9-pin Diagnostic Connector Cable](Hardware\Enclosure Design\KL68-04.pdf)
5. [PLC4TRUCKS daughter board](Hardware\SSC P485 Breakout Board\SSC_P485_Schematics.pdf)
6. [Bitmagic Basic Logic Analyzer](https://1bitsquared.com/products/bitmagic-basic)

The internals of the UTHP are as follows:

![Hardware_Internals](Hardware\UTHP Internals.png)

## BeagleBone Black
The [BeagleBone Black](https://www.beagleboard.org/boards/beaglebone-black) is development board that runs a 1GHz ARM® Cortex-A8 processor and embedded Linux. It can be purchased with the details below:

```
Manufacturer: GHI Electronics, LLC
Mfg. Part Number: BBB01-SC-505
Supplier: Digikey
Supplier Part Number: [BBB01-SC-505-ND](https://www.digikey.com/en/products/detail/ghi-electronics-llc/BBB01-SC-505/6210999)
```

A 4-pin (2x2) male header needs to be soldered to the BeagleBone Black to connect it to the supercapacitor circuit. An example of this header is the following:

```
Manufacturer: Samtec Inc.
Mfg Part Number: 87227-2
Supplier: Digikey
Supplier Part Number: [SAM10843-ND](https://www.digikey.com/en/products/detail/samtec-inc/TSW-102-07-F-D/2685865)
```

## Printed Circuit Board
The UTHP PCB is a circuit card assembly connecting all the pieces of the UTHP in the enclosure. It has the following interfaces:
1. Pins for the Beaglebone Black
2. Controller Area Network (CAN) transceivers
3. Power supply and power management
4. Local Interconnect Network (LIN) interfaces
5. Real-time clock
6. Pinouts for the J2497 (PLC4TRUCKS) daughter board
7. SAE J1708 interfaces
8. Circuit protection

These features and interfaces are shown in detail in the ![UTHP PCB v3 schematics](UTHP%20PCB\UTHP%20Truck%20Cape%20v3%20Schematics.pdf).

The PCB design was done in a tool called Altium Designer. The original files for Altum Designer are available in the .zip file of the UTHP PCB directory. To produce the PCB, an electronics assembly business will need Gerber files to have the PCBs made, a Bill of Materials for the parts to put on the PCB, and the Pick-n-Place file to show where the parts go on the PCB. These files are also included in the UTHP PCB directory. With these files, anyone can produce the UTHP. 

There are multiple hardware versions for the PCB. The design is open, but uses Altium Designer software for the PCB Layout software. Each version is captured as a schematic, Altium files, bill of materials and Gerber Files. Previous versions are archived in the Development Versions directory. 

The UTHP PCB and SSC 485 Breakout are released under the permissive [Solderpad Hardware License v2.1](http://solderpad.org/licenses/SHL-2.1/).

## Enclosure
The main part of the enclosure is the [Hammond 1455Q1602BK](https://www.digikey.com/en/products/detail/hammond-manufacturing/1455Q1602BK/965866) enclosure. This is an anodized black aluminum enclosure that can accept 160mm by 120mm printed circuit boards. The anodized aluminum is nicely finished with a laser etcher and the file that is used to etch the graphics on the top of the enclosure is available as an svg file: 

![Belly Pan Layout](Enclosure%20Design/Belly%20Pan%20Layout.svg)

There are holes  for banana jacks on the enclosure. These are drilled to accomodate the banana jack breakout board. 

The ends of the enclosure are plastic end caps that be cut with a laser. The part number for a spare end cap is [Hammond 1455QPLBK](https://www.digikey.com/en/products/detail/hammond-manufacturing/1455QPLBK/2359061)

The end caps also support the USB connections with a micro USB cable and Ethernet with RJ45. These are exposed on the end panel with an internal cable that connects directy to the BeagleBone Black.


## Internal Cables
Micro USB: [AdaFruit P/N: 3318](https://www.adafruit.com/product/3318)

Ethernet: [AdaFruit P/N: 909](https://www.adafruit.com/product/909)

USB-C: [Sparkfun P/N: CAB-15455](https://www.sparkfun.com/panel-mount-usb-c-extension-cable-6.html)

## Banana Jack Breakout Board
There is a printed circuit board mounted to the UTHP enclosure using banana jacks. The schematic simply shows it as a passthrough device to match the aligned banana jacks. A ribbon cable connects the banana jack board with the main PCB. The connecting ribbon cable is 5 inches in length to allow for disassembly and adjustment of hardware components. Both ends of each cable have female ribbon cable connectors oriented so that the number one pin aligns with the designated triangle marking on each connector. 

The breakout board exposes all the CAN channels, LIN, J1708. Raw Power and ground. The reason it's called raw power is because the power line has not been filtered and it may carry the PLC4TRUCKS (SAE J2497) signals. 

The [banana jack breakout board schematic](Enclosure%20Design/banana%20jack%20board%20schematic.pdf) shows the signals included. The [design files from Altium](Enclosure%20Design/banana%20jack%20circuit%20board%20v2.zip) include the resulting Gerber and NC Drill files. These are sufficient for someone to have these boards manufactured. 

![Rendering of Banana Jack Board](Enclosure%20Design/BananaJackBoardRendering.png)

With the printed circuit boards in hand, they need to be populated. The connector is a 20-pin shrouded male header mounted on the bottom of the board. The banana jacks themselves are mounted through the enclosure and secured in place with the nuts that come with the banana jacks. The part numbers and utilization in the breakout board are as follows:

| Quantity | Manufacturer | Mfg Part Num | Supplier | Supplier Part Num | Designation | Description |
|----------|--------------|--------------------------|----------|----------------------|-------------|-------------|
|    1     | Cal Test Electronics | CT2230-2 | Digikey | BKCT2230-2-ND | Raw (VBat)  | CONN BANANA JACK THREADED RED    |
|    1     | Cal Test Electronics | CT2230-0 | Digikey | BKCT2230-0-ND | GND         | CONN BANANA JACK THREADED BLACK  |
|    4     | Cal Test Electronics | CT2230-4 | Digikey | BKCT2230-4-ND | J1939H, CAN2H, CAN3H, CAN4H | CONN BANANA JACK THREADED YELLOW  |
|    4     | Cal Test Electronics | CT2230-5 | Digikey | BKCT2230-5-ND | J1939L, CAN2L, CAN3L, CAN4L | CONN BANANA JACK THREADED GREEN  |
|    1     | Cal Test Electronics | CT2230-6 | Digikey | BKCT2230-6-ND | J1708+   | CONN BANANA JACK THREADED BLUE  |
|    2     | Cal Test Electronics | CT2230-9 | Digikey | BKCT2230-9-ND | J1708-, LIN  | CONN BANANA JACK THREADED WHITE  |
|    1     | Molex |   70246-2001  | Digikey |  WM6548-ND  | J1 | Connector Header Through Hole 20 position 0.100" (2.54mm) |

The CT2228 series from Cal Test Electronics is a suitable substitute for the banana jacks. Alternatives to the 20 position shrouded header are also acceptable. 

## 9-pin Diagnostic Connector
The 9-pin connector is a double ended connector that is connected on the inside of the UTHP. These are custom cables made in China. The design drawing for the KL68-04 is available [here](Hardware\Enclosure Design\KL68-04.pdf). The cable is passed through a PG11 cord grip that secures the wires through the end panel. Inside, a Molex 10-pin Mini-fit Jr. connection is made to connect the cable to the board. 


| Quantity | Manufacturer | Mfg Part Num | Supplier | Supplier Part Num | Designation | Description |
|----------|--------------|--------------------------|----------|----------------------|-------------|-------------|
|    1     | Cactus Electroinics | KL68-04 | CAR LINK | KL68-04 | Cable  | Dual Headed Deutsch 9-pin Cable    |
|    1     | Molex | 39-01-2100 | Digikey | WM3704-ND | Cable End | Mini-Fit Jr 5557 10 Position Receptacle 4.20mm |
|    1     | Essentra Components | CG-PG11-2-BK | Digikey | RPC2237-ND | Cord Grip | CABLE GLAND 5-10MM PG11 POLYAMID |

## PLC4TRUCKS
The approach to working with the SAE J2497 - Power Line Carrier Communications for Commercial Vehicles was to build another specialty printed circuit board that contained the Intellon P485 chip. However, this chip is at end of life, so these PCBs may not be able to be produced in the future. The design for this board is also in this repository.  Hardware\SSC P485 Breakout Board\SSC_P485_Schematics.pdf

## Logic Analyzer
The [BitMagic Basic Logic Analyzer](https://1bitsquared.com/products/bitmagic-basic) is used inside the UTHP. There is a designated header that connects the BitMagic Basic to the signals on the board. These signals can be analyzed using the SIGROK software. The Logic analyzer is exposed through the enclosure with a USB-C cable and is not connected to the Beaglebone Black on the inside. The bitmagic basic is protected with some heat shrink and floats in the enclosure. 


## License
Copyright 2024 Jeremy Daily and Carson Green
SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1

Licensed under the Solderpad Hardware License v 2.1 (the “License”); you may not use this file except in compliance with the License, or, at your option, the Apache License version 2.0. You may obtain a copy of the License at

https://solderpad.org/licenses/SHL-2.1/

Unless required by applicable law or agreed to in writing, any work distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
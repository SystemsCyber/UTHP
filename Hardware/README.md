# Ultimate Truck Hacking Platform Hardware Design

The hardware design has the following main components:


2. BeagleBone Black
2. Printed Circuit Board
1. Enclosure: Hammond 1455
3. Banana Jack Breakout
4. 9-pin Diagnostic Connector
5. PLC4TRUCKS daughter board 
5. Internal Cables
6. FX2 Logic Analyzer
 

## BeagleBone Black
The BeagleBone Black (https://www.beagleboard.org/boards/beaglebone-black) is development board that runs a 1GHz ARM® Cortex-A8 processor and embedded Linux. It can be purchased with the details below:

```
Manufacturer: GHI Electronics, LLC
Mfg. Part Number: BBB01-SC-505
Supplier: Digikey
Supplier Part Number: BBB01-SC-505-ND
```

A 4-pin (2x2) male header needs to be soldered to the BeagleBone Black to connect it to the supercapacitor circuit. An example of this header is the following:

```
Manufacturer: Samtec Inc.
Mfg Part Number: 87227-2
Supplier: Digikey
Supplier Part Number: SAM10843-ND
```

## Printed Circuit Board
There are multiple hardware versions for the PCB. The design is open, but uses Altium Designer software for the PCB Layout software. Each version is captured as a schematic, Altium files, bill of materials and Gerber Files.

### Version 2:
Schematics: 
![UTHP Version 2 Schematics](UTHP%20PCB/UTHP%20Schematics%20v2.pdf)

Bill of Materials: 
[UTHP BOM v2.csv](UTHP%20PCB/UTHP%20BOM%20v2.csv)



### Version 1:
Schematics: 
![UTHP Version 1 Schematics](UTHP%20PCB/UTHP%20Schematics%20v1.pdf)

Photo of the top side of the board.

![UTHP V1 Topside.jpg](UTHP%20V1%20Topside.jpg)

Photo of the bottom side of the board.

![UTHP V1 Bottomside.jpg](UTHP%20V1%20Bottomside.jpg)

#### Version 1 Errata:
1. The LEDs needs to be moved towards the center of the board to keep the LEDs from interering with the light pipes.
2. The DSUB15 connector needs to be moved towards the edge of the board.
3. There are many other changes that make version 1 of the board unsuitable for use.

## Enclosure
The main part of the enclosure is the [Hammond 1455Q1602BK](https://www.digikey.com/en/products/detail/hammond-manufacturing/1455Q1602BK/965866) enclosure. This is an anodized black aluminum enclosure that can accept 160mm by 120mm printed circuit boards. The anodized aluminum is nicely finished with a laser etcher and the file that is used to etch the graphics on the top of the enclosure is available as an svg file: 

![Belly Pan Layout](Enclosure%20Design/Belly%20Pan%20Layout.svg)

There are holes layed out for banana jacks on the enclosure. These are drilled to accomodate the banana jack breakout board. 

The ends of the enclosure are plastic end caps that be cut with a laser. The part number for a spare end cap is [Hammond 1455QPLBK](https://www.digikey.com/en/products/detail/hammond-manufacturing/1455QPLBK/2359061)

The end caps also support the USB connections with a micro USB cable and Ethernet with RJ45. These are exposed on the end panel with an internal cable that connects directy to the BeagleBone Black.

Micro USB P/N: 3318 link: https://www.adafruit.com/product/3318

Ethernet P/N: 909 link: https://www.adafruit.com/product/909

## Banana Jack Breakout Board
There is a printed circuit board mounted to the UTHP enclosure using banana jacks. The schematic simply shows it as a passthrough device to match the aligned banana jacks. A ribbon cable connects the banana jack board with the main PCB. 

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
The 9-pin connector is a double ended connector that is connected on the inside of the UTHP. These are custom cable made in China. The design drawing for the KL68-04 is available here. The cable is passed through a cord grip that secures the wires through the end panel. Inside, a Molex 10-pin Mini-fit Jr. connection is made to connect the cable to the board. 


| Quantity | Manufacturer | Mfg Part Num | Supplier | Supplier Part Num | Designation | Description |
|----------|--------------|--------------------------|----------|----------------------|-------------|-------------|
|    1     | Cactus Electroincs | KL68-04 | CAR LINK | KL68-04 | Cable  | Dual Headed Deutsch 9-pin Cable    |
|    1     | Molex | 39-01-2100 | Digikey | WM3704-ND | Cable End | Mini-Fit Jr 5557 10 Position Receptacle 4.20mm |
|    1     | Essentra Components | CG-PG11-2-BK | Digikey | RPC2237-ND | Cord Grip | CABLE GLAND 5-10MM PG11 POLYAMID |

## PLC4TRUCKS
There are two approaches to working with the SAE J2497 - Power Line Carrier Communications for Commercial Vehicles. The first approach is to use a GPIO pin through the PRU to excite and read the PLC signals through a coupling capacitor. The second approach is to utilize purpose build hardware for PLC communication. 

The hardware approach has 2 solutions: 1) a custom circuit board for the Intellion P485 chip that has been used in PLC enable devices for many years, and 2) a new Mikroe Click board using the SM24000 PLC solution. 

## Logic Analyzer
The [BitMagic Basic Logic Analyzer](https://1bitsquared.com/products/bitmagic-basic) is used inside the UTHP. There is a designated header that connects the BitMagic Basic to the signals on the board. These signals can be analyzed using the SIGROK software. 

A small micro USB cable is needed to connect the Bitmagic to the Beagle Bone Black. For example: the [DH-20M50057 from Cvilux](https://www.digikey.com/en/products/detail/cvilux-usa/DH-20M50057/13177527).

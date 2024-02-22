# RISC-V-Object-Tracker

**Required Hardware**
![image](https://github.com/EricSiaSiewWei/RISC-V-Object-Tracker/assets/136912487/762184d8-77b8-41d4-a140-5be1535ebc13)
1. StarFive VisionFive2 Single Board Computer (SBC) - 4GB RAM
2. Cubeternet GL-UPC822 UVC Webcam
3. Xeme WiFi6 Dongle
4. 5V DC Brushless Fan
5. Raspberry Pi Official USB-C Power Supply
6. Kingston Memory Card 100MB/s 32GB Micro SD Card
7. Kingston Micro SD Card Reader 

**Installed Software Application**
1. UltraVNC Viewer
2. Python Integrated Development and Learning Environment (IDLE)
3. Google Colaboratory  

**Operating System**
Debian 12 (bookworm)

**List of Optional Hardware**
1. Viewsonic 24" VX2428J LCD Gaming Monitor
2. LEAVEN Mechanical Keyboard
3. Vention HDMI Cable 2.0
4. GAMING FREAK Silent Mouse XX4 

**User Guide:**
Step 1: Flashing Debian OS
VisionFive 2 supports several boot modes through SD image, NVMe (Non-Volatile Memory express) image, embedded MultiMediaCard (eMMC) image and Universal Asynchronous Receiver / Transmitter (UART). Nevertheless, SD card-based boot approach has been executed due to its simplicity, as it is a similar approach in setting up a Raspberry PI board.
1. Browse for latest engineering release from StarFive at Microsoft OneDrive link: https://debian.starfivetech.com/
2. Navigate towards SD card section and download the Debian image pre-built by StarFive.
3. Download BalenaEtcher application.
4. Open BalenaEtcher software, in the meantime, insert a 32-GB micro-SD card into the laptop using USB micro-SD card reader. Ensure the selected SD storage is the targeted card.
5. Extract the .img file from the downloaded .zip file from Step 2. Upload the image file to BalenaEtcher and start the flash task.
6. After finish writing the disk image, a successfully flash message appears further indicates that the 32-GB micro-SD card is ready to be ejected from laptop and to be inserted into SD card slot of VisionFive 2.


Step 2: Logging into Debian
Table 1: Boot Modes Settings
| Index  | Boot Mode  | RGPIO_1 | RGPIO_0 |
| :------------ |:---------------:| -----:| -----:|
| 1 | 1-bit QSPI Nor Flash | 0 (L) | 0 (L) |
| 2 | SDIO3.0        |   0 (L) | 1(H) |
| 3 | eMMC        |    1(H) | 0 (L) |
| 3 | UART        |    1(H) | 1(H) |
1. Perform the setup shown below
![image](https://github.com/EricSiaSiewWei/RISC-V-Object-Tracker/assets/136912487/a9ebd624-cf41-4934-b3ba-e3d90df1bb4e)![image](https://github.com/EricSiaSiewWei/RISC-V-Object-Tracker/assets/136912487/9e762dc3-2e7d-4212-982f-bddff6be17b6)
2. Connect Raspberry Pi Official USB-C Power Supply into VisionFive 2 USB C port. For first time setup, it is essential to connect VisionFive2 SBC to monitor through High-Definition Multimedia Interface (HDMI) cable.
3. There are 4 types of boot modes, namely 1-bit QSPI Nor Flash, UART, eMMC and SDIO3.0 based on Table 1. Select the boot mode SDIO with Rapid General-Purpose Input/Output Drivers (RGPIO) configuration as followed:
        RGPIO_1: 0 (LOW) and RGPIO_0: 1 (HIGH).
![image](https://github.com/EricSiaSiewWei/RISC-V-Object-Tracker/assets/136912487/a9ebd624-cf41-4934-b3ba-e3d90df1bb4e)![image](https://github.com/EricSiaSiewWei/RISC-V-Object-Tracker/assets/136912487/9e762dc3-2e7d-4212-982f-bddff6be17b6)
4. A Gnome login interface appears which prompts user to enter the credentials as follows. Open Terminal Emulator after successful login.
        Username: user
        Password: starfive

Step 3: Remote Access Setup
To ease the usage of VisionFive 2 SBC, it is essential to mirror a its interface screen to an IP-based screen mirroring software like UltraVNC for remote access, not to mention its benefits of easing data recording operations between the two operating systems, especially copying and pasting operations. Furthermore, screen mirroring removes the need to connect the peripheral devices such as monitor, keyboard and mouse to the SBC which can contribute to additional power consumption on VisionFive 2.
1. Ensure USB WiFi adaptor is plugged into the peripheral I/O port of VisionFive2 SBC. Navigate to the network section in setting and connect to a known WiFi. Akin to command 'ipconfig' applied in Windows OS, command 'nmcli -p device show' used to show the IP address of VisionFive 2 SBC. Record the IP address '192.168.137.244'. Note the IP address may vary upon connection to different WiFi network.
2. Enter privileged mode (root).
3. Install UltraVNC viewer on client laptop. Back to VisionFive 2 SBC, install a standalone TigerVNC server.
4. Exit privileged mode and install the MATE Desktop Environment.
5. When setting up a VNC, it is essential for user to set a VNC password. In this context, the VNC password is set as 'starfive'.
6. Initiate the VNC server with MATE desktop, screen resolution [1920x1080], display number 1.
7.  Return to client laptop, insert the IP address recorded from STEP 1 into the section, with a format (Server's hostname or IP address):(display number). Press connect and enter password 'starfive' for input authentication. A successful login will be verified by the pop up of Debian OS home page.
8.  After every usage, it is optional for user to either manually kill the TigerVNC server or perform shutdown at start icon to close the connection between client laptop with VisionFive2 SBC.

Step 4: Software Libraries


Step 5: Testing & Troubleshooting


Step 6: Implementation



# RISC-V-Object-Tracker

**Required Hardware**
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
  Step 1.1:  Browse for latest engineering release from StarFive at Microsoft OneDrive link: https://debian.starfivetech.com/ 
  Step 1.2:  Navigate towards SD card section and download the Debian image pre-built by StarFive.
  Step 1.3: Download BalenaEtcher application. 
  Step 1.4: Open BalenaEtcher software, in the meantime, insert a 32-GB micro-SD card into the laptop using USB micro-SD card reader. Ensure the selected SD storage is the targeted card.
  Step 1.5: Extract the .img file from the downloaded .zip file from step 1.2. Upload the image file to BalenaEtcher and start the flash task.
  Step 1.6: After finish writing the disk image, a successfully flash message appears further indicates that the 32-GB micro-SD card is ready to be ejected from laptop and to be inserted into SD card slot of VisionFive 2.


Step 2: Hardware Setup
  Step 2.1:  Logging into Debian
| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |

Step 3: Software Libraries

Step 4: Testing & Troubleshooting

Step 5: Implementation



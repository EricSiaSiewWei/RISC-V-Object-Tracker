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

Step 4: Expanding the rootfs partition 
1. It is essential to check the usable space on memory compartment (32-GB SD card). If the available usable space of SD card at /dev/mmcblk1p4 is mismatched with the expected specification (usually smaller), several commands are needed to expand the unused space on the SD card. This is important to enable user to install any relevant libraries for future works.

Step 5: Software Libraries
1.At Terminal (non-root mode), install the essential packages provided by StarFive. In this context, user will obtain browsers such as Firefox and Chromium, VLC and FFmpeg as media player, and others packages include node.js, v8, libsdl2-dev, GStreamer, v4l2test, Libreoffice, QT and NW.js. Some of these essential packages provided by StarFive are not available to download via apt/apt-get. To improve overall user experience, install vim and nautilus (Gnome File Viewer) and upgrade several existing packages.
wget https://github.com/starfive-tech/Debian/releases/download/v0.8.0-engineering-release-wayland/install_package_and_dependencies.sh
chmod +x install_package_and_dependencies.sh
nano install_package_and_dependencies.sh
sudo ./install_package_and_dependencies.sh

Table 2: Essential Packages provided by StarFive.
| Library                                 | Purpose                         |
| :-------------------------------------- | :------------------------------ |
| libxslt1.1                              | LibreOffice Runtime Dependency  |
| openjdk-11-jdk                          | LibreOffice Runtime Dependency  |
| libmd4c-dev                             | QT Runtime Dependency           |
| libdouble-conversion-dev                | QT Runtime Dependency           |
| libc6-dev                               | QT Runtime Dependency           |
| libpcre2-16-0                           | QT Runtime Dependency           |
| "^libxcb.*"                             | QT Runtime Dependency           |
| libx11-xcb-dev                          | QT Runtime Dependency           |
| libglu1-mesa-dev                        | QT Runtime Dependency           |
| libxrender-dev                          | QT Runtime Dependency           |
| libxi-dev                               | QT Runtime Dependency           |
| libxkbcommon-x11-dev                    | QT Runtime Dependency           |
| libevent-dev                            | Firefox Runtime Dependency      |
| libdbus-glib-1-dev                      | Firefox Runtime Dependency      |
| libopenal-dev                           | FFMPEG Runtime Dependency       |
| libcdio-paranoia-dev                    | FFMPEG Runtime Dependency       |
| libdc1394-dev                           | FFMPEG Runtime Dependency       |
| libcaca-dev                             | FFMPEG Runtime Dependency       |
| libv4l-dev                              | FFMPEG Runtime Dependency       |
| libpocketsphinx-dev                     | FFMPEG Runtime Dependency       |
| libbs2b-dev                             | FFMPEG Runtime Dependency       |
| liblilv-0-0                             | FFMPEG Runtime Dependency       |
| librubberband-dev                       | FFMPEG Runtime Dependency       |
| libmysofa-dev                           | FFMPEG Runtime Dependency       |
| libflite1                               | FFMPEG Runtime Dependency       |
| libass-dev                              | FFMPEG Runtime Dependency       |
| libvidstab-dev                          | FFMPEG Runtime Dependency       | 
| libzmq3-dev                             | FFMPEG Runtime Dependency       | 
| libzimg-dev                             | FFMPEG Runtime Dependency       |
| libgme-dev                              | FFMPEG Runtime Dependency       |
| libopenmpt-dev                          | FFMPEG Runtime Dependency       |
| libchromaprint-dev                      | FFMPEG Runtime Dependency       |
| librabbitmq-dev                         | FFMPEG Runtime Dependency       |
| libssh-dev                              | FFMPEG Runtime Dependency       |
| libsrt-openssl-dev                      | FFMPEG Runtime Dependency       |
| liba52-0.7.4-dev                       | FFMPEG Runtime Dependency        |
| libhwy1                                 | FFMPEG Runtime Dependency       |
| libjxl0.7                               | FFMPEG Runtime Dependency       |
| libv4l-0                                | v4l2test Runtime Dependency     |
| libjpeg-dev                             | v4l2test Runtime Dependency     |
| libdrm-dev                              | v4l2test Runtime Dependency     |
| libv4l-0                                | v4l2test Runtime Dependency     |
| libjpeg-dev                             | v4l2test Runtime Dependency     |
| libdrm-dev                              | v4l2test Runtime Dependency     |
| libv4l-0                                | v4l2test Runtime Dependency     |
| libjpeg-dev                             | v4l2test Runtime Dependency     |
| libdrm-dev                              | v4l2test Runtime Dependency     |
| libre2-9                                | chromium Runtime Dependency     |
| libminizip-dev                          | chromium Runtime Dependency     |
| fonts-mathjax                           | opencv Runtime Dependency       |
| libjs-mathjax                           | opencv Runtime Dependency       |
| libpython3.11-minimal                   | opencv Runtime Dependency       |
| libpython3.11-stdlib                    | opencv Runtime Dependency       |
| python3-numpy                           | opencv Runtime Dependency       |
| python3.11                              | opencv Runtime Dependency       |
| python3.11-minimal                      | opencv Runtime Dependency       |
| python3-h5py                            | opencv Runtime Dependency       |
| libvtk9.1                               | opencv Runtime Dependency       |
| libqt5test5                             | opencv Runtime Dependency       |
| libqt5opengl5                           | opencv Runtime Dependency       |
| libtesseract5                           | opencv Runtime Dependency       |
| libgdcm-dev                             | opencv Runtime Dependency       |
| libgdal-dev                             | opencv Runtime Dependency       |
| gstreamer1.0-clutter-3.0                | cogl/clutter Runtime Dependency |
| fonts-freefont-ttf                      | vlc Runtime Dependency          |
| libaribb24-0                            | vlc Runtime Dependency          |
| libcddb2                                | vlc Runtime Dependency          |
| libdvbpsi10                             | vlc Runtime Dependency          |
| libebml5                                | vlc Runtime Dependency          |
| libixml10                               | vlc Runtime Dependency          |
| liblirc-client0                         | vlc Runtime Dependency          |
| liblua5.2-0                             | vlc Runtime Dependency          |
| libmad0                                 | vlc Runtime Dependency          |
| libmatroska7                            | vlc Runtime Dependency          |
| libprotobuf-lite32                      | vlc Runtime Dependency          |
| libqt5x11extras5                        | vlc Runtime Dependency          |
| libresid-builder0c2a                    | vlc Runtime Dependency          |
| libsdl-image1.2                         | vlc Runtime Dependency          |
| libsdl1.2debian                         | vlc Runtime Dependency          |
| libsidplay2                             | vlc Runtime Dependency          |
| libspatialaudio0                        | vlc Runtime Dependency          |
| libupnp13                               | vlc Runtime Dependency          |
| libva-wayland2                          | vlc Runtime Dependency          |
| libvncclient1                           | vlc Runtime Dependency          |
| :-------------------------------------- | :------------------------------ |
 
2. Install essential python libraries via command "pip install" or "sudo apt-get install". These libraries support the the operations of OpenCV Legacy Trackers, YOLOv7 and YOLOv8.
Table 3: Essential Python Libraries supporting OpenCV Legacy Trackers, YOLOv7 and YOLOv8.
| Package                              | Version             |
| :----------------------------------- | :-----------------: |
| antlr4-python3-runtime               | 4.9.3               |
| appdirs                              | 1.4.4               |
| astunparse                           | 1.6.3               |
| attrs                                | 22.2.0              |
| av                                   | 10.0.0              |
| Babel                                | 2.10.3              |
| beautifulsoup4                       | 4.11.1              |
| beniget                              | 0.4.1               |
| bottle                               | 0.12.23             |
| Bottleneck                           | 1.3.2               |
| Brotli                               | 1.0.9               |
| certifi                              | 2022.9.24           |
| chardet                              | 5.1.0               |
| charset-normalizer                   | 3.0.1               |
| cycler                               | 0.11.0              |
| decorator                            | 5.1.1               |
| defusedxml                           | 0.7.1               |
| distro                               | 1.8.0               |
| docker                               | 5.0.3               |
| et-xmlfile                           | 1.0.1               |
| exceptiongroup                       | 1.0.4               |
| fonttools                            | 4.37.4              |
| fs                                   | 2.4.16              |
| future                               | 0.18.2              |
| gast                                 | 0.5.2               |
| Glances                              | 3.3.0.1             |
| h5py.-debian-h5py-serial             | 3.7.0               |
| html5lib                             | 1.1                 |
| hub-sdk                              | 0.0.3               |
| idna                                 | 3.3                 |
| influxdb                             | 5.3.1               |
| iniconfig                            | 1.1.1               |
| jdcal                                | 1.0                 |
| Jinja2                               | 3.0.3               |
| kiwisolver                           | 1.3.2               |
| lxml                                 | 4.9.1               |
| lz4                                  | 4.0.2+dfsg          |
| MarkupSafe                           | 2.1.1               |
| matplotlib                           | 3.5.2               |
| more-itertools                       | 8.10.0              |
| mpmath                               | 0.0.0               |
| msgpack                              | 1.0.3               |
| netifaces                            | 0.11.0              |
| numexpr                              | 2.8.4               |
| numpy                                | 1.23.5              |
| odfpy                                | 1.4.2               |
| olefile                              | 0.46                |
| omegaconf                            | 2.3.0               |
| openpyxl                             | 3.0.9               |
| packaging                            | 21.3                |
| pandas                               | 1.3.5               |
| patsy                                | 0.5.3               |
| Pillow                               | 9.2.0               |
| pip                                  | 23.3.2              |
| pluggy                               | 1.0.0+repack        |
| ply                                  | 3.11                |
| psutil                               | 5.9.4               |
| py                                   | 1.11.0              |
| py-cpuinfo                           | 9.0.0               |
| pyasn1                               | 0.4.8               |
| pycryptodomex                        | 3.11.0              |
| Pygments                             | 2.13.0              |
| pyparsing                            | 3.0.9               |      
| pysmi                                | 0.3.2               |
| pysnmp                               | 4.4.12              |
| pystache                             | 0.6.0               |
| pytest                               | 7.2.0               |
| python-dateutil                      | 2.8.2               |
| pythran                              | 0.11.0              |
| pytz                                 | 2022.7              |
| PyYAML                               | 6.0.1               |
| requests                             | 2.28.1              |
| SciPy                                | 1.8.1               |
| seaborn                              | 0.12.1              |
| setuptools                           | 65.5.0              |
| six                                  | 1.16.0              |
| soupsieve                            | 2.3.2               |
| sympy                                | 1.11.1              |
| tables                               | 3.7.0               |
| tomli                                | 2.0.1               |
| torch                                | 1.12.0a0+gitunknown |
| torchvision                          | 0.13.1a0            |
| tqdm                                 | 4.66.1              |
| types-aiofiles                       | 22.1                |
| types-annoy                          | 1.17                |
| types-appdirs                        | 1.4                 |
| types-aws-xray-sdk                   | 2.10                |
| types-babel                          | 2.11                |
| types-backports.ssl-match-hostname   | 3.7                 |
| types-beautifulsoup4                 | 4.11                |
| types-bleach                         | 5.0                 |
| types-boto                           | 2.49                |
| types-braintree                      | 4.17                |
| types-cachetools                     | 5.2                 |
| types-caldav                         | 0.10                |
| types-certifi                        | 2021.10.8           |
| types-cffi                           | 1.15                |
| types-chardet                        | 5.0                 |
| types-chevron                        | 0.14                |
| types-click-spinner                  | 0.1                 |
| types-colorama                       | 0.4                 |
| types-commonmark                     | 0.9                 |
| types-console-menu                   | 0.7                 |
| types-contextvars                    | 2.4                 |
| types-croniter                       | 1.3                 |
| types-cryptography                   | 3.3                 |
| types-D3DShot                        | 0.1                 |
| types-dateparser                     | 1.1                 |
| types-DateTimeRange                  | 1.2                 |
| types-decorator                      | 5.1                 |
| types-Deprecated                     | 1.2                 |
| types-dj-database-url                | 1.0                 |
| types-docopt                         | 0.6                 |
| types-docutils                       | 0.19                |
| types-editdistance                   | 0.6                 |
| types-emoji                          | 2.1                 |
| types-entrypoints                    | 0.4                 |
| types-first                          | 2.0                 |
| types-flake8-2020                    | 1.7                 |
| types-flake8-bugbear                 | 22.10.27            |
| types-flake8-builtins                | 2.0                 |
| types-flake8-docstrings              | 1.6                 |
| types-flake8-plugin-utils            | 1.3                 |
| types-flake8-rst-docstrings          | 0.2                 |
| types-flake8-simplify                | 0.19                |
| types-flake8-typing-imports          | 1.14                |
| types-Flask-Cors                     | 3.0                 |
| types-Flask-SQLAlchemy               | 2.5                 |
| types-fpdf2                          | 2.5                 |
| types-gdb                            | 12.1                |
| types-google-cloud-ndb               | 1.11                |
| types-hdbcli                         | 2.14                |
| types-html5lib                       | 1.1                 |
| types-httplib2                       | 0.21                |
| types-humanfriendly                  | 10.0                |
| types-invoke                         | 1.7                 |
| types-JACK-Client                    | 0.5                 |
| types-jmespath                       | 1.0                 |
| types-jsonschema                     | 4.17                |
| types-keyboard                       | 0.13                |
| types-ldap3                          | 2.9                 |
| types-Markdown                       | 3.4                 |
| types-mock                           | 4.0                 |
| types-mypy-extensions                | 0.4                 |
| types-mysqlclient                    | 2.1                 |
| types-oauthlib                       | 3.2                 |
| types-openpyxl                       | 3.0                 |
| types-opentracing                    | 2.4                 |
| types-paho-mqtt                      | 1.6                 |
| types-paramiko                       | 2.11                |
| types-parsimonious                   | 0.10                |
| types-passlib                        | 1.7                 |
| types-passpy                         | 1.0                 |
| types-peewee                         | 3.15                |
| types-pep8-naming                    | 0.13                |
| types-Pillow                         | 9.3                 |
| types-playsound                      | 1.3                 |
| types-polib                          | 1.1                 |
| types-prettytable                    | 3.4                 |
| types-protobuf                       | 3.20                |
| types-psutil                         | 5.9                 |
| types-psycopg2                       | 2.9                 |
| types-pyaudio                        | 0.2                 |
| types-PyAutoGUI                      | 0.9                 |
| types-pycurl                         | 7.45                |
| types-pyfarmhash                     | 0.3                 |
| types-pyflakes                       | 2.5                 |
| types-Pygments                       | 2.13                |
| types-pyinstaller                    | 5.6                 |
| types-PyMySQL                        | 1.0                 |
| types-pynput                         | 1.7                 |
| types-pyOpenSSL                      | 22.1                |
| types-pyRFC3339                      | 1.1                 |
| types-PyScreeze                      | 0.1                 |
| types-pysftp                         | 0.2                 |
| types-pytest-lazy-fixture            | 0.6                 |
| types-python-crontab                 | 2.6                 |
| types-python-dateutil                | 2.8                 |
| types-python-gflags                  | 3.1                 |
| types-python-jose                    | 3.3                 |
| types-python-nmap                    | 0.7                 |
| types-python-slugify                 | 6.1                 |
| types-pytz                           | 2022.6              |
| types-pyvmomi                        | 7.0                 |
| types-pywin32                        | 304                 |
| types-PyYAML                         | 6.0                 |
| types-redis                          | 4.3                 |
| types-regex                          | 2022.10.31          |
| types-requests                       | 2.28                |
| types-retry                          | 0.9                 |
| types-Send2Trash                     | 1.8                 |
| types-setuptools                     | 65.5                |
| types-simplejson                     | 3.17                |
| types-singledispatch                 | 3.7                 |
| types-six                            | 1.16                |
| types-slumber                        | 0.7                 |
| types-SQLAlchemy                     | 1.4.43              |
| types-stdlib-list                    | 0.8                 |
| types-stripe                         | 3.5                 |
| types-tabulate                       | 0.9                 |
| types-termcolor                      | 1.1                 |
| types-toml                           | 0.10                |
| types-toposort                       | 1.7                 |
| types-tqdm                           | 4.64                |
| types-tree-sitter                    | 0.20                |
| types-tree-sitter-languages          | 1.5                 |
| types-ttkthemes                      | 3.2                 |
| types-typed-ast                      | 1.5                 |
| types-tzlocal                        | 4.2                 |
| types-ujson                          | 5.5                 |
| types-urllib3                        | 1.26                |
| types-vobject                        | 0.9                 |
| types-waitress                       | 2.1                 |
| types-whatthepatch                   | 1.0                 |
| types-xmltodict                      | 0.13                |
| types-xxhash                         | 3.0                 |
| types-zxcvbn                         | 4.4                 |
| typing_extensions                    | 4.3.0               |
| ufoLib2                              | 0.13.1              |
| ultralytics                          | 8.0.196             |
| unicodedata2                         | 15.0.0              |
| urllib3                              | 1.26.12             |
| webencodings                         | 0.5.1               |
| websocket-client                     | 1.2.3               |
| wheel                                | 0.38.4              |
| xlwt                                 | 1.3.0               |
| vim                                  |2:9.0.0813-1+b1      |
| :----------------------------------- | :-----------------: |

Step 5: Testing & Troubleshooting


Step 6: Implementation



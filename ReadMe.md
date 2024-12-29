# Raspberry RTC with Temp

## Documentation

### Temp sensor AHT10
https://www.instructables.com/ROOM-TEMP-Meter-With-Arduino-Nano-and-AHT10/

### I2C bus
https://github.com/fivdi/i2c-bus/blob/master/doc/raspberry-pi-software-i2c.md
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
https://forums.raspberrypi.com/viewtopic.php?t=354655
https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/

### GPIO
https://projects.raspberrypi.org/en/projects/physical-computing/1


### RTC circuit
https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi?view=all


### NTP Server
https://rishabhdevyadav.medium.com/how-to-install-ntp-server-and-client-s-on-ubuntu-18-04-lts-f0562e41d0e1


### NTP Client
https://forums.raspberrypi.com/viewtopic.php?t=308207
https://askubuntu.com/questions/254826/how-to-force-a-clock-update-using-ntp
https://www.baeldung.com/linux/sync-time-with-network


### Display TFT 0.96"
https://www.mouser.com/datasheet/2/1398/Soldered_333099-3395096.pdf?srsltid=AfmBOopo9jPX7zSLOix_c1GKDUoyYUEk6n7hLzhsUK3vsUmG7P1-zE4b
https://github.com/RUDEWORLD/Pi5OLED/blob/14601d2e8573b905423d541818ee103462035a53/INSTALL%20I2C%20OLED%20ON%20Pi5%20BOOKWORM.md
https://github.com/SolderedElectronics/Soldered-OLED-Display-Arduino-Library
https://www.recantha.co.uk/blog/?p=18463


## Software dependencies

### Packages to  install 
sudo apt-get install i2c-tools
sudo apt-get install -y python3-smbus
sudo apt-get install build-essential python-dev python-pip python-imaging python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
sudo apt-get install python3-pip
sudo apt install --upgrade python3-setuptools
sudo apt install python3-venv
sudo apt-get install python3-pil


### Python packages to install
sudo pip3 install adafruit-circuitpython-ssd1306
pip3 install adafruit-python-shell
pip3 install adafruit-blinka
pip3 install adafruit-io
sudo pip3 install --break-system-packages adafruit-blinka

git clone https://github.com/adafruit/Adafruit_Python_SSD1306
sudo python3 setup.py install
pip3 install Adafruit_GPIO
pip3 install Adafruit_SSD1306
pip install Pillow


## Pre install tasks
### Run raspi-config and enable I2C interfac
sudo raspi-config
sudo i2cdetect -y 0


## Installation












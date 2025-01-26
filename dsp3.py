
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from gpiozero import LED

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
from datetime import datetime
import subprocess
from ntptimenow import NTPTimeNow

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used

# Note you can change the I2C address by passing an i2c_address parameter like:
#disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x50)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()
led = LED(20)
led.off()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

led.on()
time.sleep(4)
led.off()

time.sleep(0.2)
led.on()
time.sleep(2)
led.off()

time.sleep(0.5)
led.on()
time.sleep(1)
led.off()

time.sleep(0.5)
led.on()
time.sleep(0.5)
led.off()

time.sleep(0.5)
led.on()
time.sleep(0.25)
led.off()


# Load default font.
font = ImageFont.load_default()

while True:
    top = 0
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    dt1 = datetime.now()
    #now = NTPTimeNow(poolservers='se.pool.ntp.org', version=3)
    now = NTPTimeNow(poolservers='192.168.86.128', version=3)
    dt2 = datetime.now()
    line1 = f'{str(dt1)[11:-1]}' 
    line2 = f'{str(dt2)[11:-1]}' 
    line3 = f'{str(now.ntp_now())[11:-1]}'
    del1 = dt2 -dt1
    del2 = now.ntp_now() - dt1
    if (del2.microseconds > 50000):
        led.on()
        time.sleep(0.5)
        led.off()
    line4 = f'{str(del2)}'
    line5 = f'{str(del1)}' 

    draw.text((x, top),    line1, font=font, fill=255)
    draw.text((x, top+10), line2, font=font, fill=255)
    draw.text((x, top+20), line3, font=font, fill=230)
    draw.text((x, top+30), line4, font=font, fill=240)
    draw.text((x, top+40), line5, font=font, fill=240)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(5)

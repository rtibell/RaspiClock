
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from gpiozero import LED
import paho.mqtt.client as mqtt

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
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Load default font.
font = ImageFont.load_default()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)
    print(f"Subscribing on topic {TOPIC}")

def on_message(client, userdata, msg):
    dsp_msg = msg.payload.decode()
    print(f"Message received from topic {msg.topic} : {dsp_msg}")
    dsp_line(dsp_msg)

def dsp_line(msg):
    line = ["" for _ in range(10)]
    acc_len = 0
    line_nr = 0
    splt = msg.split(" ")
    print(f"splitt {splt}")
    for sp in splt:
        if (acc_len + len(sp) + 1 > 20):
            line_nr = line_nr + 1
            line[line_nr] = sp
            acc_len = len(sp)
        else:
            line[line_nr] = line[line_nr] + " " + sp
            acc_len = len(line[line_nr])
    top = 0
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    for li in line:
        draw.text((x, top), li, font=font, fill=255)
        top = top + 20
    disp.image(image)
    disp.display()
    

# MQTT
BROKER_ADDRESS = "192.168.86.253"
BROKER_PORT = 1883
TOPIC = "test/mqtt-zero"

# Create MQTT client
client = mqtt.Client()

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

try:
    client.connect(BROKER_ADDRESS, BROKER_PORT)
    client.loop_forever()
except keyboardInterrupt:
    print("Problem, exiting")
    client.disconnect()

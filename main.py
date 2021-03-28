from machine import Pin, I2C, freq
import ssd1306
#from time import sleep
import time
import dht
import machine
import os
import socket
from class_temp import TempHum

print('CPU:', freq()) 


# ESP32
#i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# ESP8266
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def sleep_time(func):
    def wrapper():
        func()
        time.sleep(1)
    return wrapper



@sleep_time
def show():
    show_ = oled.show()
   
@sleep_time
def poweron():
    poweron_ = oled.poweron()

@sleep_time
def blank_lcd():
    off = oled.poweroff()

pin = Pin(2, Pin.OUT)
def blink(sec):
    pin.off()
    time.sleep(sec)
    pin.on()
   


#x = 5
#while x != 0:
while True:
        
#  d = dht.DHT22(machine.Pin(12))
#  d.measure()
  #print('temp:', d.temperature())
  #print('hum:', d.humidity())    
  #x -= 1
  blink(1)
  
  t = TempHum().temp()
  h = TempHum().hum()
  # output to lcd
  oled.text('TEMP:{}C'.format(TempHum().temp()), 30, 0)
  oled.text('HUM:{}H'.format(TempHum().hum()), 30, 20)
  # socket
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.0.165', 8888))
  except OSError:
    print('not server connection')
    blank_lcd()
    poweron()
    oled.text('not server',0,0)
    show()
    break
  except KeyboardInterrupt:
    blank_lcd()
    break
  else:  
  # bytes
  
    t = bytes(t, 'utf8')
    h = bytes(h, 'utf8')
    # output to serv
    sock.send('Temperature: {} C '.format(t.decode()))
    sock.send('Humidity: {} %'.format(h.decode()))

    res = sock.recv(1024)
    
    print('answer from server:', res.decode())
    sock.close()


    show()
      # polling time
    time.sleep(60)
     
    


#  commands

#oled.invert(True)
#oled.fill(1)

#show()
#blank_lcd()
#poweron()


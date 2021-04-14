from machine import Pin, I2C, freq
import ssd1306
#from time import sleep
import time
import dht
import machine
import os
import socket


#from class_temp import TempHum

print('CPU:', freq()) 


# ESP32
#i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# ESP8266
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
i2c2 = I2C(-1, scl=Pin(0), sda=Pin(2))
oled_width = 128
#oled_height = 64
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)



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



global iter
iter = 0
timesleeping = 60

#x = 5
#while x != 0:
while True:
        
    d = dht.DHT22(machine.Pin(12))
    d.measure()
    #print('temp:', d.temperature())
    #print('hum:', d.humidity())    
  #x -= 1
    blink(1)
    oled.fill(0)
    t = d.temperature()
    h = d.humidity()
    fan = None
  # output to lcd
    oled.text('TEMP:{}C'.format(str(t)), 0, 0)
    oled.text('HUM:{}%'.format(str(h)), 0, 10)
    oled.text('FAN:{}'.format(fan), 0, 20)
    
    
  # socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.0.165', 8888))
        oled.text('tcp', 85, 0)
        oled.text('ok', 85, 8)
        
    except OSError:
        print('not server connection')
        oled.fill(0)
        iter = int(iter) + 1
        oled.text('TEMP:{}C'.format(str(t)), 0, 0)
        oled.text('HUM:{}%'.format(str(h)), 0, 10)
        oled.text('FAN:{}'.format(fan), 0, 20)
        oled.text('not', 85, 0)
        oled.text('conn..', 85, 8)
        oled.text('#{}'.format(iter), 85, 20)
        show()
        time.sleep(timesleeping)
    except KeyboardInterrupt:
        blank_lcd()
        break
    else:  
    # bytes
  
#        t = bytes(t, 'utf8')
#        h = bytes(h, 'utf8')
      # output to serv
        sock.send('Temperature: {} C '.format(t))
        sock.send('Humidity: {} %'.format(h))

        res = sock.recv(1024)
    
        print('answer from server:', res.decode())
        sock.close()

    
        show()
#        oled.fill(1)
#            
      
        time.sleep(timesleeping) # polling time
#        blank_lcd()
#        time.sleep(1)
#        poweron()
#        show() 



#  commands

#oled.invert(True)
#oled.fill(1)

#show()
#blank_lcd()
#poweron()


import dht
from machine import Pin

class TempHum:
    """get measure"""
    d = dht.DHT22(Pin(12))
    d.measure()

    def temp(self):
        temp = self.d.temperature()
        return str(temp)

    def hum(self):
        hum = self.d.humidity()
        return str(hum)



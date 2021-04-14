#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
#webrepl.start()
gc.collect()

import main

#from network import WLAN
#import network

#wlan = WLAN()
#nets = wlan.scan()
#if nets == None:
#    print('no wifi')
#print(nets)
## enable station interface and connect to WiFi access point
#nic = network.WLAN(network.STA_IF)
#nic.active(True)
#nic.connect('wifi', '22224444')
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('wifi', '22224444')
        while not wlan.isconnected():
            main()
    print('network config:', wlan.ifconfig())

do_connect()

main()
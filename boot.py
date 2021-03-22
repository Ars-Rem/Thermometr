#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
webrepl.start()
gc.collect()


import network
from network import WLAN



wlan = WLAN()


nets = wlan.scan()
print(nets)
for net in nets:
    print(net)
    if net == 'wifi':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, ''), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
    else:
        pass



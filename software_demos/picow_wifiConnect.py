import network
import socket
from time import sleep
import machine

ssid = 'MicroPython-2e61a8'
password = 'micropythoN'



def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    accesspoints = wlan.scan()
    for ap in accesspoints:
         print(ap)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        print(wlan.status())
        sleep(1)
        wlan.connect(ssid, password)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip


try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()
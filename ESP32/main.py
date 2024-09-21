# Escreva o seu código aqui :-)
# from machine import Pin, TouchPad
#import time
#import saida
#import entrada
#import esp32
#import _thread as T
#import esp32_MQTT
#import thingspeak
#import mqtt_client
import subscriber
import mqtt
#import mqtt_ssl_tls
#from time import sleep
#import main1
import net
#import mqtt_speak







####WIFIMGR#######teste


import wifimgr
wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D
            # Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")        
#####WIFIMGR#####

import webrepl
webrepl.start()
#import webrepl_setup


import _thread as th




#net.do_connect("vivo-1001","19752013")#('Multilaser_WS01','lanudo1902')#
# rotina de loop para executar 
def com ():
    while True:
        mqtt.mqtt()
        subscriber.main()
        
def speak ():
    import mqtt_speak1
    mqtt_speak1()
    
#th.start_new_thread(wifi_1,())    
th.start_new_thread(com,())
th.start_new_thread(speak,())



#import main
import machine
import urequests 
from machine import Pin
import network, time
import dht
from time import sleep
global temperature
global humidity
HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'XXXXXXXXX'
#UPDATE_TIME_INTERVAL = 10000  # in ms 
#last_update =  time.ticks_ms() 
#last_update = time.ticks_ms()


def speak():

    for i in range (1):
        

        try:
            temperature=0
            humidity=0
            sensor = dht.DHT22(Pin(2))
            sleep(0.3)
            sensor.measure()
            print(sensor.temperature(),sensor.humidity())
            temperature=sensor.temperature()
            humidity=sensor.humidity()
            
                     
        except OSError as e:
            print('Failed to read sensor.')
            
            
        if temperature and humidity >1:    
            try:
                print('enviando variaveis para nuvem THINGSPEAK')
                bme_readings = {'field1':temperature,'field2':humidity} #'field1':temperature, 'field2':humidity,
                request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = bme_readings, headers = HTTP_HEADERS )  
                request.close()
                print(bme_readings)
                print('finalizando envio THINGSPEAK')
            except OSError as y:
                print('erro de requisição')
              
                pass

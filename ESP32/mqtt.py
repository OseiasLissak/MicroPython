"""
MicroPython IoT Weather Station Example for Wokwi.com

To view the data:

1. Go to http://www.hivemq.com/demos/websocket-client/
2. Click "Connect"
3. Under Subscriptions, click "Add New Topic Subscription"
4. In the Topic field, type "wokwi-weather" then click "Subscribe"

Now click on the DHT22 sensor in the simulation,
change the temperature/humidity, and you should see
the message appear on the MQTT Broker, in the "Messages" pane.

Copyright (C) 2022, Uri Shaked

https://wokwi.com/arduino/projects/322577683855704658
"""
#import dht
def mqtt (): 
    from machine import Pin
    from umqtt.simple import MQTTClient
    import ujson
    import esp32
    #import network
    import time
    #import machine import Pin
    #import ussl as ssl
    import saida
    import dht
    botao=Pin(0)

    # MQTT Server Parameters
    MQTT_CLIENT_ID = "julxxx"
    MQTT_BROKER    = 'broker.hivemq.com'#"
    MQTT_USER      = ''##'xxxxxx'
    MQTT_PASSWORD  = ''#'xxxxx'
    MQTT_TOPIC     = "xxxxx"
    MQTT_PORT      = ""
    MQTT_KEEP     = 40 #,keepalive=MQTT_KEEP
    #objetos
    sensor = dht.DHT11(Pin(15))
    #led=Pin(2,Pin.OUT)
    print("Connecting to MQTT server... ", end="")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD,  keepalive = MQTT_KEEP,ssl=False)
    client.connect()
    print("Connected!")
    
    i=0
    for i in range (3):
        try:
            print("Measuring weather conditions... ", end="")
            saida.ledon(1)
            time.sleep(1)
            sensor.measure()  
            print(sensor.temperature(),sensor.humidity())            
            message = ujson.dumps({
            "temp": sensor.temperature(),
            "humidity": sensor.humidity(),
            })
            saida.ledon(0)
            time.sleep(1)    
            print("Updated!")
            print("Reporting to MQTT topic {}: {}".format(MQTT_TOPIC, message))
            client.publish(MQTT_TOPIC, message)
            client.subscribe(liga)
            client.subscribe(desliga)
        except:
            print('falha de leitura')
                
    client.disconnect()
    print('disconectado')





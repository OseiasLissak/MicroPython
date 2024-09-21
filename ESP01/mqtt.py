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
    import main
    #import esp32
    #import network
    import time
    #import utime
    import machine 
    #import ussl as ssl
    #import main
    import dht
    #botao=Pin(0)

    # MQTT Server Parameters
    MQTT_CLIENT_ID = "jul"
    MQTT_BROKER    = 'broker.hivemq.com'#"a71085617fbad8b.s2.eu.hivemq.cloud"
    MQTT_USER      = ''##'XXXXXXXXX'
    MQTT_PASSWORD  = ''#'XXXXX'
    MQTT_TOPIC     = "XXXXXX"
    MQTT_PORT      = ""
    MQTT_KEEP     = 40 #,keepalive=MQTT_KEEP
    
    #objetos
    pin_dht = 2  # Substitua pelo pino ao qual o sensor DHT22 está conectado

# Configuração do objeto DHT
    dht_sensor = dht.DHT22(machine.Pin(pin_dht))
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    print("Temperatura: {:.2f} °C".format(temperature))
    print("Umidade: {:.2f} %".format(humidity))
    
    if  4 <= temperature <=6:
        print('temperatura no set point - ok')
        
    if temperature <= 3:
        print ('ALERTA - TEMPERATURA MUITO BAIXA') 
        print ('COLOQUE A MEDICAÇÂO NA PRATELEIRA ABAIXO OU BAIXE O TERMOSTATO DA GELADEIRA')
        alertabaixa=1
    else:
        alertabaixa=0
                
    if temperature >= 7:
        print ('ALERTA - TEMPERATURA MUITO ALTA')
        print ('VERIFIQUE SE A GELADEIRA ESTA LIGADA, MANTENHA A PORTA FECHADA POR ALGUNS MINUTOS')
        alertaalta=1
    else:
        alertaalta=0

    print("Connecting to MQTT server... ", end="")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD,  keepalive = MQTT_KEEP,ssl=False)
    try:
        client.connect()
        print("Connected!")
        i=0
        for i in range (3):
            try:
                
                print("medindo temperatura e humidade... ", end="")
                dht_sensor.measure() 
                print(dht_sensor.temperature(),dht_sensor.humidity(),alertaalta,alertabaixa)
                
                message = ujson.dumps({
                "temp": dht_sensor.temperature(),
                "humidity": dht_sensor.humidity(),
                "alertaa": alertaalta,
                "alertab": alertabaixa
                })
               
                time.sleep(2)
                print("Reporting to MQTT topic {}: {}".format(MQTT_TOPIC, message))
                print('enviando mensagem json para nuvem')
                client.publish(MQTT_TOPIC, message)
                print("mensagem enviada!")
                
            except Exception as e:
                print("Erro:", e)
                #pass
                return
    #        except:
        #        print('falha de leitura')
            #    pass  
        client.disconnect()
        print('mqtt disconectando.........')
        
        
    except Exception as e:
        print("Erro:", e)
        #pass
        return
#    except:
   #     print('falha de conexão ou de transmissão- mqtt/linha 47')
   #     pass
       

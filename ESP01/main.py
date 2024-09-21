import dht
import machine
import time
import net_v2
import speak
import network
import mqtt
#import _thread
#import net
#net.do_connect('vivo-1001','19752013')
sta_if = network.WLAN(network.STA_IF)
# Configuração do pino de dados do sensor DHT22
pin_dht = 2  # Substitua pelo pino ao qual o sensor DHT22 está conectado

# Configuração do objeto DHT
dht_sensor = dht.DHT22(machine.Pin(pin_dht))

# Função para ler e imprimir os dados do sensor
def read_dht_data():
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        print("Temperatura: {:.2f} °C".format(temperature))
        print("Umidade: {:.2f} %".format(humidity))    
    except Exception as e:
        print("Erro ao ler dados do sensor DHT22:", str(e))
# Loop principal

while True:
    try:
        speak.speak()
        mqtt.mqtt()
        
        #read_dht_data()
        #wdt.feed()
        
        #wdt.feed()
        #mqtt.mqtt()
        print('aguardando 5 minutos para continuar')
        time.sleep(300)#wdt.feed()
        net_v2.check_internet_connection()
        
        
        
        
    except Exception as e:
        print("Erro:", e)
        machine.reset()

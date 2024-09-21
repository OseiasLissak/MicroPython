import network
import urequests
import machine
# Função para conectar-se à rede WiFi
def connect_to_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    #if sta_if.isconnected() == False:    
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
            
        sta_if.connect(ssid,password)
        # Espera até que a conexão seja estabelecida
        while not sta_if.isconnected():
            pass
        
            
        print('network config:', sta_if.ifconfig())
        

    print('Conectado com sucesso à rede WiFi:', ssid)
    print('Configuração IP:', sta_if.ifconfig())

# Conecte-se à sua rede WiFi
SSID = "XXXXX"  # Substitua pelo nome da sua rede WiFi
PASSWORD = "XXXXXX"  # Substitua pela senha da sua rede WiFi
connect_to_wifi(SSID, PASSWORD)

# Função para configurar um IP fixo na rede interna
def set_static_ip(ip, mask, gateway):
    sta_if = network.WLAN(network.STA_IF)
    _, _, _, dns = sta_if.ifconfig()  # Obtém o DNS atual da configuração DHCP
    sta_if.ifconfig((ip, mask, gateway, dns))
    print('Configuração de IP estático aplicada:', sta_if.ifconfig())

# Configure um IP fixo na rede interna
IP = '192.168.0.120'  # Substitua pelo IP fixo desejado
MASK = '255.255.255.0' 
GATEWAY = '192.168.0.1'
set_static_ip(IP, MASK, GATEWAY)

# Função para verificar a conexão com a internet
def check_internet_connection():
    try:
        response = urequests.get("http://www.google.com")
        if response.status_code == 200:
            print("Conexão com a internet está OK!")
        else:
            print("Houve um problema ao verificar a conexão com a internet.")
            print("Rebooting ESP01...")
            machine.reset()
    except Exception as e:
        print("Erro ao verificar a conexão com a internet:", e)
        print("Rebooting ESP01...")
        machine.reset()

# Verifique a conexão com a internet
#set_static_ip(IP, MASK, GATEWAY)

check_internet_connection()

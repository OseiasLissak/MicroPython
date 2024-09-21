

def botao1(pin):
    global bo1 
    bo1=bool
    
    from machine import Pin, TouchPad
    from time import sleep
    #while True:
    touch=TouchPad(Pin(pin)) #pin 32 botao touch
    #touch_value= touch.read()
    #while True:
    
    
    while True:
   # if bo1 == 0:
        touch_value= touch.read()
        #print(touch_value,bo1)
        #sleep (0.5)
        if touch_value <=250:
            if bo1 !=1:
                led = Pin(2, Pin.OUT)
                led.value(1)
                print('botão 1 ligado')
                
                bo1=1
                #touch_value= touch.read()
                #print(touch_value,bo1)
                sleep(1)
                for i in range (10):
                    #print(touch_value,bo1)
                    touch_value= touch.read()
                #sleep(2)
                
                
                
        if touch_value <=250:        
            if bo1 == 1:
                led = Pin(2, Pin.OUT)
                led.value(0)
                print('botão 1 desligado')
                bo1=0
                #touch_value= touch.read()
                #print(touch_value,bo1)
                sleep(1)
                for i in range (10):
                    #print(touch_value,bo1)
                    touch_value= touch.read()
                #sleep(2)
    #return bo1
    #entrada.botao1(32) # STATUS EM MEMORIA B01

   # if bo1 == 1:
        
   # if bo1 == 0:
       
       # saida.ledon(0)    
    
# Atribuir a uma variável o GPIO2 como pino de saída
#led = Pin(2, Pin.OUT)


    

#if sta_if.isconnected() 
#led1 = Pin(4, Pin.OUT)







import Adafruit_DHT
import time
from signal import signal,SIGTERM,SIGHUP,pause
from rpi_lcd import LCD
DHT_SENSOR=Adafruit_DHT.DHT11
DHT_PIN=4
lcd=LCD()
def safe_exit(signum,frame):
    exit(1)
    
signal(SIGTERM,safe_exit)
signal(SIGHUP,safe_exit)
while True:
    #Read DHT11 Readings
    humidity,temperature=Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
    if humidity is not None and temperature is not None:
        message1="Tem: "+'{:1.2f}'.format(temperature)+"C"
        message2="HU: "+'{:1.2f}'.format(humidity)+"%"
        print("Temperature= {0:0.1f}C Humidity={1:0.1f}%".format(temperature,humidity))
        lcd.text(message1,1)
        lcd.text(message2,2)
        
    
    else:
        print("Error")
        
   
     

    time.sleep(3)
        
    

import Adafruit_DHT
from datetime import datetime
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

if humidity is not None and temperature is not None:
	file = open("/home/airquality/Desktop/Sensor_R_CSV/log.csv","a")
	file.write("{0:0.2f}".format(temperature)+","+"{0:0.2f}".format(humidity)+",")

# else:
# 	file = open("/home/airquality/Desktop/Sensor_R_CSV/log.csv","a")
# 	file.write("NAN     "+",")
# 
# file.write(datetime.today().strftime('%Y-%m-%d'+"," '%H:%M:%S')+"\n")
file.close()
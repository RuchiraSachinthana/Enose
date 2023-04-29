
import Adafruit_DHT
import time
import datetime
import Adafruit_ADS1x15
from datetime import datetime
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk


adc = Adafruit_ADS1x15.ADS1115()

fig, ax = plt.subplots()
x, y = [], []
line, = ax.plot([], [])

def animate(i):
    values = [0]*4
    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN)
    x.append(datetime.now())
    y.append(values[0])
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

def start_process():
    #Motor pump machanism start
    channel = 24
    Wtime = int(e1.get())
    label = e2.get()
    fradius = e3.get()
    flenth = e4.get()
   

    # GPIO setup
    GPIO.setwarnings(False)  # Suppress warnings
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)

    def motor_on(pin):
        GPIO.output(pin, GPIO.HIGH)  # Turn motor on
    def motor_off(pin):
        GPIO.output(pin, GPIO.LOW)  # Turn motor off

    motor_on(channel)
    start_time = datetime.now()
    while (datetime.now() - start_time).seconds < Wtime:
        humidity,temperature=Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
        if humidity is not None and temperature is not None:  
            print ("Date and Time : " + datetime.today().strftime('%Y-%m-%d'+"," '%H:%M:%S'))
            print( "DHT11 : "  + "Temperature = {0:0.1f}C Humidity = {1:0.1f}% Label = {2} Radius = {2} Lenth = {2}".format(temperature,humidity, label, fradius, flenth))
        
        else:
            print("Error")

        values = [0]*4
        for i in range(4):
        
            values[i] = adc.read_adc(i, gain=GAIN)
    
        print("================================================================= \n")   
        print(' MQ2:  {0:>6} \n MQ7 : {1:>6} \n MQ135:{2:>6} \n MQ3 : {3:>6} \n '.format(*values))
        print("=================================================================")
        file = open("/home/airquality/Desktop/Sensor_R_CSV/enosedataNONRipedDATA3.csv","a")
        #file.write("Date,Time,MQ2,MQ7,MQ135,MQ3,Temperature,Humidity, Label, Radius, Lenth") # Headers for CSV File
        file.write(datetime.today().strftime('%Y-%m-%d'+"," '%H:%M:%S'))
        #file.write("{0:>6},{1:>6},{2:>6}".format(*values)+",{0:0.2f}".format(temperature)+" "+",{0:0.2f}".format(humidity)+"\n" )
        file.write("{0:>6},{1:>6},{2:>6}, {3:>6}".format(*values)+ " " + ",{0:0.2f}".format(temperature)+" "+",{0:0.2f}".format(humidity) + " " + ",{0}".format(label)  + " " + ",{0}".format(fradius) + " " + ",{0}".format(flenth) + "\n" )
        #file.write("{0}".format(label) + ", {0:>6},{1:>6},{2:>6}, {3:6}".format(*values)+",{0:0.2f}".format(temperature)+" "+",{0:0.2f}".format(humidity)+"\n" )
        file.close()
    
   
    time.sleep(5)
    motor_off(channel)
    time.sleep(5)
    GPIO.cleanup()

    #MPM Stop

   # plt.show()

# clean the system

def clean_system():
    # GPIO setup
    GPIO.setwarnings(False)  # Suppress warnings
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)

    # Turn motor on for 60 seconds
    GPIO.output(24, GPIO.HIGH)
    time.sleep(60)

    # Turn motor off
    GPIO.output(24, GPIO.LOW)
    time.sleep(1)

    # Clean up GPIO
    GPIO.cleanup()



# Set up GUI
root = tk.Tk()
root.title("E-Nose Data Collection")

tk.Label(root, text="Enter Time in seconds:").grid(row=0, column=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)

tk.Label(root, text="Enter the Lable number:").grid(row=1, column=0)
e2 = tk.Entry(root)
e2.grid(row=1, column=1)

tk.Label(root, text="Enter the radius in |cm| :").grid(row=2, column=0)
e3 = tk.Entry(root)
e3.grid(row=2, column=1)

tk.Label(root, text="Enter the lenth in |cm| :").grid(row=3, column=0)
e4 = tk.Entry(root)
e4.grid(row=3, column=1)


get_data_button = tk.Button(root, text="GET DATA", command=start_process)
get_data_button.grid(row=5, column=0, columnspan=2)

clean_button = tk.Button(root, text="CLEAN THE SYSTEM", command=clean_system)
clean_button.grid(row=6, column=0, columnspan=2)



# Set up ADC
GAIN = 1

DHT_SENSOR=Adafruit_DHT.DHT11
DHT_PIN= 6

# Set up plot
ani = FuncAnimation(fig, animate, interval=1000)

root.mainloop()

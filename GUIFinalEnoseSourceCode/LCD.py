from signal import signal,SIGTERM,SIGHUP,pause
from rpi_lcd import LCD
lcd=LCD()
def safe_exit(signum,frame):
    exit(1)
    
signal(SIGTERM,safe_exit)
signal(SIGHUP,safe_exit)
try:
    lcd.text("Air Quality",1)
    lcd.text("TEST",2)
    pause()
     
     
except keyboardinterrupt:
    pass
finally:
    lcd.clear()
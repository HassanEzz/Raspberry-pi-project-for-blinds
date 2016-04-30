import RPi.GPIO as GPIO
import picamera
from time import*
GPIO.setmode(GPIO.BOARD)
GPIO.setup (12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
camera = picamera.PiCamera()
i=1
while True:
    
    input_state = GPIO.input(12)
    if input_state ==False:
        print('khaled'+str(i)+'.jpg')
        camera.capture ('khaled'+str(i)+'.jpg')        
        i=i+1
        sleep(0.2)
    



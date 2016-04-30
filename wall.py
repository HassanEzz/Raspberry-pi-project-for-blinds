import RPi.GPIO as GPIO
import time
import pygame
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False) 
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.OUT)

pygame.mixer.init()
pygame.mixer.music.load('/home/pi/beep1.ogg')


while True:
    GPIO.output(10, False)
    time.sleep(0.3)
    GPIO.output(10, True)
    time.sleep(0.001)
    GPIO.output(10, False)

    while GPIO.input(8)==0:
        signalOff=time.time()
    while GPIO.input(8)==1:
        signalOn=time.time()
    timepassed=signalOn-signalOff
    distance=timepassed*17150
    print distance
    if distance <15:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy()==True:
            continue
                              
GPIO.cleanup()

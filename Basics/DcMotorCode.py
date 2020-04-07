import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class motor():
    def __init__(self,Ena,In1,In2):
        self.Ena = Ena
        self.In1 = In1
        self.In2 = In2
        GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        self.pwm = GPIO.PWM(self.Ena, 100)
        self.pwm.start(0)
    def moveF(self,x=100,t=0):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.HIGH)
        GPIO.output(self.In2,GPIO.LOW)
        sleep(t)
    def moveB(self,x=100,t=0):
        self.pwm.ChangeDutyCycle(x)
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.HIGH)
        sleep(t)
    def stop(self,t=0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)

motor1 = motor(2,3,4)

while True:
   
    motor1.moveF(30,2)
    motor1.stop(1) 
    motor1.moveB(t=2)
    motor1.stop(1)
    
    '''
    for x in range(20,100):
        motor1.moveF(x,0.05)
        print(x)
    for x in range(100,20,-1):
        motor1.moveF(x,0.05)
        print(x)
    motor1.stop(5)
    '''
    

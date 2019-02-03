import RPi.GPIO as GPIO
from time import sleep

class Garage:
    'The interface for the garage door'

    def __init__(self, output_pin):
        self.output_pin = output_pin

        if not GPIO.getmode():
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.output_pin, GPIO.OUT, initial=GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

    def activate(self):
        GPIO.output(self.output_pin, GPIO.HIGH)
        sleep(2)
        GPIO.output(self.output_pin, GPIO.LOW)

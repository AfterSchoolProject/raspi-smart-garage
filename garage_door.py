import RPi.GPIO as GPIO
from time import sleep

class GarageDoor:
    'The interface for the garage door'

    def __init__(self, channel):
        self.channel = channel
        self.status = "closed"

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.channel, GPIO.OUT)

    def open(self):
        if self.status != "open":
            self.__activate()

    def close(self):
        if self.status != "closed":
            self.__activate()

    def cleanup(self):
        GPIO.cleanup(self.channel)

    def __activate(self):
        GPIO.output(self.channel, GPIO.LOW)
        sleep(1)
        GPIO.output(self.channel, GPIO.HIGH)

import RPi.GPIO as GPIO
from time import sleep

class Garage:
    'The interface for the garage door'

    def __init__(self, input_pin, output_pin):
        self.input_pin = input_pin
        self.output_pin = output_pin

        if not GPIO.getmode():
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(
                self.input_pin,
                GPIO.IN,
                pull_up_down=GPIO.PUD_DOWN
            )
            GPIO.setup(self.output_pin, GPIO.OUT, initial=GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

    def activate(self):
        activated = False
        GPIO.output(self.output_pin, GPIO.HIGH)

        tries = 3
        while tries > 0:
            if GPIO.input(self.input_pin) == True:
                activated = True
                print("Garage is activated")
                break
            sleep(0.2)
            tries -= 1
        GPIO.output(self.output_pin, GPIO.LOW)

        return activated

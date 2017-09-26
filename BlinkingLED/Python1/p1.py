import RPi.GPIO as GPIO
import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

GPIO.output(7, True)
time.sleep(1)
GPIO.output(7, False)
time.sleep(1)
GPIO.output(7, True)
time.sleep(1)
GPIO.output(7, False)

print "Done"

GPIO.cleanup()


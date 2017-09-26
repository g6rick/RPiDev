import RPi.GPIO as GPIO
import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def Blink(numTimes,speed):
	for i in range(0, numTimes):
		print "Iteration " + str(i+1)
		GPIO.output(7, True)
		time.sleep(speed)
		GPIO.output(7, False)
		time.sleep(speed)
	print "Done"
	GPIO.cleanup()

iterations = raw_input("Enter number of blinks: ")
speed = raw_input("Enter blink length (seconds): ")

Blink(iterations, float(speed))

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

from crawl.brain import find_wall_in_front
from crawl import drive

try:
	find_wall_in_front()
	# while True:
	# 	drive.sharp_turn_left()
except KeyboardInterrupt:
	GPIO.cleanup()

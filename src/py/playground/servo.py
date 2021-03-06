import RPi.GPIO as GPIO
import time

SERVO_PIN = 33
DISTANCE_IN_PIN = 32
DISTANCE_OUT_PIN = 31
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(DISTANCE_OUT_PIN, GPIO.OUT)
GPIO.setup(DISTANCE_IN_PIN, GPIO.IN)
p = GPIO.PWM(SERVO_PIN, 50)
p.start(2.5)


def turn(angle):
	dut_cycle = 2.5 + angle / 18.0
	p.ChangeDutyCycle(dut_cycle)


def distance():
	GPIO.output(DISTANCE_OUT_PIN, True)
	time.sleep(0.000002)
	GPIO.output(DISTANCE_OUT_PIN, False)

	while not GPIO.input(DISTANCE_IN_PIN):
		pass
	start = time.time()

	while GPIO.input(DISTANCE_IN_PIN):
		pass
	return (time.time() - start) * 17150


def scan_around():
	while True:
		angle = 0
		while angle < 180:
			turn(angle)
			print("angle = " + str(angle) + "; distance=" + str(distance()) + " cm")
			angle += 45
			time.sleep(0.1)
		while angle > 0:
			turn(angle)
			print("angle = " + str(angle) + "; distance=" + str(distance()) + " cm")
			angle -= 45
			time.sleep(0.1)


def angle_distance():
	turn(0)
	print(str(distance()))
	p.stop()
	GPIO.cleanup()


try:
	time.sleep(0.1)
	# scan_around()
	angle_distance()
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

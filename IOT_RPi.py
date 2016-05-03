import os
import time
import RPi.GPIO as GPIO


class RPiControl:
	'Control anything connected to relay/RPi GPIO pins (BCM mode)'
	
	os.system('modprobe w1-gpio')
	os.system('modprobe w1-therm')
	#set up GPIO using BCM numbering
	GPIO.setmode(GPIO.BCM)
	#GPIO.setwarnings(False)

		
	
	# intialise class
	def __init__(self, pin, sensor, temp):
		
		self.pin = pin  # input the pin number control relay
		self.sensor = sensor # Temp sensor file location
		self.temp = temp #input the incubation temperature


	def set_pin(self):  
		GPIO.setup(self.pin, GPIO.OUT) ## Setup GPIO Pin  to OUT
		#'/sys/bus/w1/devices/28-00042b6579ff/w1_slave'


	def temp_raw(self):
		temp_sensor = self.sensor ##Setup sensor file location
		f = open(temp_sensor, 'r')
		lines = f.readlines()
		f.close()
		return lines

	def read_temp(self):
		lines = self.temp_raw()
		while lines[0].strip()[-3:] != 'YES':
			time.sleep(0.2)
			lines = self.temp_raw();
		temp_output = lines[1].find('t=')
		if temp_output != -1:
			temp_string = lines[1].strip()[temp_output+2:]
			temp_c = float(temp_string) / 1000.0
		return temp_c


	def temp_control(self):
		while (True):
			print (self.read_temp())
			if self.read_temp() < self.temp :
				GPIO.output(17,False) ## Turn on GPIO pin 7
				time.sleep(0.5)
				print 'heating'
			elif self.read_temp() >= self.temp:
				GPIO.output(17,True) ## Turn on GPIO pin 7
				time.sleep(0.5)
				print 'cooling'
	
	#GPIO.cleanup()
	
	
#usage:
#from temp_class import RPiControl
#pin = RPiControl(17,'/sys/bus/w1/devices/28-00042b6579ff/w1_slave',37)
#pin.set_pin()
#pin.temp_control()
#	






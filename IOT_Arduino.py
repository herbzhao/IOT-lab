import serial
import time


class ArduinoControl:
	'several defined control functions'

#default value
	ser = ''
 
	def __init__(self, port):
		self.port = port
	
	def set_serial(self):
		self.ser = serial.Serial(self.port,9600)
		time.sleep(2)  #serial port needs 2 sec to be ready
  
	def led_on(self):
		self.ser.write('H')
		self.led_status = True
	
	def led_off(self):
		self.ser.write('L')
		self.led_status = False
   
#usage of this class
#serial = ArduinoControl('/dev/cu.wchusbserialfa140')

#from IOT import ArduinoControl
#port = '/dev/cu.wchusbserialfa140'
#serial.set_serial()
#ArduinoControl.led_on()


class RPiControl:
	'several defined control functions'
	def __init__(self, pin):
		pass
  

	 

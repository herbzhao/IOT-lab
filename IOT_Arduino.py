import serial
import time


class ArduinoControl:
	'connect to Arduino through serial port'

#default value
	ser = ''
 
	def __init__(self, port):
		self.port = port
#		self.command = command
	
	def set_serial(self):
		self.ser = serial.Serial(self.port,9600)
		self.sub = self.ser
		time.sleep(2)  #serial port needs 2 sec to be ready
  
  
	def led_on(self):
		self.ser.write('H')
		self.led_status = True

	def led_off(self):
		self.ser.write('L')
		self.led_status = False
		
	def excute(self,command): 									#input anything to serial port
		self.ser.write(command.encode('ascii'))	   #anything is defined by port = ArduinoControl('COM1','H')
#		self.serial_output = self.command	
   
#.encode('ascii') encoding   
#usage of this class
#port = ArduinoControl('/dev/cu.wchusbserialfa140')

#port = ArduinoControl('/dev/cu.wchusbserialfa140','H')
#port.set_serial()
#port.ser_input()

#ArduinoControl.led_on()


class RPiControl:
	'several defined control functions'
	def __init__(self, pin):
		pass
  

	 

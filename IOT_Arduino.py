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
		#self.ser = serial.Serial(self.port,9600)
		self.ser = serial.Serial()
		self.ser.port = self.port
		self.ser.baudrate = 9600
		self.ser.timeout = 1
		self.ser.dsrdtr=False
		self.ser.setDTR(False)
		self.ser.open()


	def close_port(self):
		self.ser.close()
  
	#~ def led_on(self):
		#~ self.ser.write('H')
		#~ self.led_status = True

	#~ def led_off(self):
		#~ self.ser.write('L')
		#~ self.led_status = False
																#~ #anything is defined by port = ArduinoControl('COM1')
	def excute(self,command): 									#input anything to serial port
		self.ser.write(command.encode('ascii'))
	
	def monitor(self):		
		result = str(self.ser.readline())
		result  = result.translate(None, '\n')
		result  = result.translate(None, '\r')
		voltage = {'value':result}
		return voltage
		


   
#.encode('ascii') encoding   
#usage of this class
#port = ArduinoControl('/dev/cu.wchusbserialfa140')

#port = ArduinoControl('/dev/cu.wchusbserialfa140','H')
#port.set_serial()
#port.ser_input()

#ArduinoControl.led_on()



	 

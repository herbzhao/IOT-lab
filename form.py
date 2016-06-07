from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField   # all types of forms
from wtforms import validators, ValidationError   # validator for input



class ContactForm(Form):
	Port = TextField('Arduino serial port', default = '/dev/ttyUSB0')
	
	set_serial = SubmitField("Set Serial Port")  # Click button to set serial port
	
	port_command = TextField('Any command to Arduino', default = '')
	
	send_command = SubmitField("Send command")    # click button to send command through serial

#	LED = RadioField('LED switch', choices = [(1,'ON'),(2,'OFF')], default=2)
	
	led_button_on = SubmitField("LED switch_on")    # click button to swtich on/off LED
	led_button_off = SubmitField("LED switch_off")    # click button to swtich on/off LED
	
	
	relay_pin = TextField('Pin to control relay', default = '17')
	
	sensor_location = TextField('file location for sensor', default = '/sys/bus/w1/devices/28-00042b6579ff/w1_slave')
	
	set_sensor = SubmitField("Reading from sensor")    # click button to change incubator temperature setting
	
	Temperature = TextField('Incubator temperature', default = '37')
	
	incubate = SubmitField("Start incubation")    # click button to change incubator temperature setting
	
	terminate = SubmitField("Stop incubation")    # click button to change incubator temperature setting
	
	
	
	
	
	
	
	
	

#	Port = TextField('Arduino serial port')
    
 #  LED = RadioField('LED switch', choices = [(True,'ON'),(2,'OFF')], default=0)
      
#   Platform = SelectField('System', choices = [('RPi', 'Raspberry Pi'),('Arduino', 'Arduino')])
   


   
   
#   Address = TextAreaField("Address")
   
#   email = TextField("Email",[validators.Required("Please enter your email address."),
#      validators.Email("Please enter your email address.")])
   
#   Age = IntegerField("age")




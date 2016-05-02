from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField   # all types of forms
from wtforms import validators, ValidationError   # validator for input



class ContactForm(Form):
	Port = TextField('Arduino serial port',[validators.Required("Specify serial port.")])
   
	LED = RadioField('LED switch', choices = [(1,'ON'),(2,'OFF')], default=2)
	
	SetSerial = SubmitField("Set Serial Port")  # Click button to set serial port
	
	led_button = SubmitField("LED switch")    # click button to swtich on/off LED
	

#	Port = TextField('Arduino serial port')
    
 #  LED = RadioField('LED switch', choices = [(True,'ON'),(2,'OFF')], default=0)
      
#   Platform = SelectField('System', choices = [('RPi', 'Raspberry Pi'),('Arduino', 'Arduino')])
   


   
   
#   Address = TextAreaField("Address")
   
#   email = TextField("Email",[validators.Required("Please enter your email address."),
#      validators.Email("Please enter your email address.")])
   
#   Age = IntegerField("age")




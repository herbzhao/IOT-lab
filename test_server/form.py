from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField   # all types of forms
from wtforms import validators, ValidationError   # validator for input



class ContactForm(Form):

	
	start = SubmitField("start timer")  # Click button to set serial port

	stop = SubmitField("stop timer")    # click button to send command through serial
	
	test = SubmitField("test jquery working")    # click button to send command through serial


	
	
	
	
	
	
	
	
	

#	Port = TextField('Arduino serial port')
    
 #  LED = RadioField('LED switch', choices = [(True,'ON'),(2,'OFF')], default=0)
      
#   Platform = SelectField('System', choices = [('RPi', 'Raspberry Pi'),('Arduino', 'Arduino')])
   


   
   
#   Address = TextAreaField("Address")
   
#   email = TextField("Email",[validators.Required("Please enter your email address."),
#      validators.Email("Please enter your email address.")])
   
#   Age = IntegerField("age")




from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField   # all types of forms
from wtforms import validators, ValidationError    # validator for input



class ContactForm(Form):
	Port = TextField('Arduino serial port')
   
	LED = RadioField('LED switch', choices = [(1,'ON'),(2,'OFF')], default=2)

#	Port = TextField('Arduino serial port')
    
 #  LED = RadioField('LED switch', choices = [(True,'ON'),(2,'OFF')], default=0)
      
#   Platform = SelectField('System', choices = [('RPi', 'Raspberry Pi'),('Arduino', 'Arduino')])
   
	SetSerial = SubmitField("Set Serial Port")
	led_on = SubmitField("led on")
	led_off = SubmitField("led off")
   
   
#   Address = TextAreaField("Address")
   
#   email = TextField("Email",[validators.Required("Please enter your email address."),
#      validators.Email("Please enter your email address.")])
   
#   Age = IntegerField("age")




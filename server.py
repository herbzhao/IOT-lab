from flask import Flask, render_template, request, flash
from form import ContactForm
from IOT_Arduino import ArduinoControl
from IOT_RPi import RPiControl


app = Flask(__name__)
app.secret_key= 'waterscope'


# few variables initialise


@app.route("/led", methods = ['GET', 'POST'])
def contact():
	# few variables initialise
	form =  ContactForm()
	global SerialPort
	
	
	if request.method == 'POST':	
	#Change default value once user input  something
		form.Port.default = form.Port.data
		form.LED.default = form.LED.data
		form.Temperature.default = form.Temperature.data
			
		# Press set serial button
		if 'SetSerial' in request.form: 
			# initialise Arduino serial port
			SerialPort = ArduinoControl(form.Port.data)
			SerialPort.set_serial()
			# return to HTML page once submit
			return render_template('led.html', form = form)
		
		
		# Press Led_switch button			
		elif 'led_button' in request.form:
		# radio button to control LED
			if form.LED.data == '1':
				SerialPort.led_on()
			elif form.LED.data == '2':
				SerialPort.led_off()		
			return render_template('led.html', form = form)
			
		elif 'SetTemp' in request.form:
			Pass
			
	
	elif request.method == 'GET':
		return render_template('led.html', form = form)

#serialport = ArduinoControl('/dev/cu.wchusbserialfa140')
#ArduinoControl.set_serial(SerialPort)
#ArduinoControl.led_on(SerialPort)


if __name__ == "__main__":
#	app.run(host='0.0.0.0', port=80, debug=True)
	app.run(host='10.0.0.1', port=80, debug=True)


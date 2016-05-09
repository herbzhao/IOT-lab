from flask import Flask, render_template, request, flash, jsonify
from flask import redirect, url_for, session
from form import ContactForm
from IOT_Arduino import ArduinoControl
import serial

#from IOT_RPi import RPiControl

app = Flask(__name__)
app.secret_key= 'waterscope'



# few variables initialise


@app.route("/IOT", methods = ['GET', 'POST'])
def contact():
	global serial_port
	# few variables initialise
	form =  ContactForm()
	if request.method == 'POST':	
	#Change default value once user input  something
		form.Port.default = form.Port.data
		form.port_command.default = form.port_command.data
		form.LED.default = form.LED.data
		form.Temperature.default = form.Temperature.data
		# Press set serial button
		
		
		if 'set_serial' in request.form: 
			# initialise Arduino serial port
			serial_port = ArduinoControl(form.Port.data)
			serial_port.set_serial()
			# return to HTML page once submit
			return render_template('index.html', form = form)
		
		
		# Press send command to serial button
		# This allows form to send any command to arduino
		# Configure arduino code for this
		
		if 'send_command' in request.form: 
			# excute command
  			serial_port.excute(form.port_command.data)
			# return to HTML page once submit
			return render_template('index.html', form = form)


		# Press Led_switch button			
		elif 'led_button' in request.form:
		# radio button to control LED
			if form.LED.data == '1':
				serial_port.led_on()
			elif form.LED.data == '2':
				serial_port.led_off()		
			return render_template('index.html', form = form)
			
		# Press temperature change
		elif 'set_temp' in request.form:
			pass
			
		#initialise the form
	elif request.method == 'GET':
		return render_template('index.html', form = form)
		
		


@app.route('/result')
def serial_monitor():
	global serial_port
	voltage = serial_port.monitor()
	return jsonify(voltage)


if __name__ == "__main__":
#	app.run(host='0.0.0.0', port=80, debug=True)
	#app.run(host='10.0.0.1', debug=True)
	app.run(debug=True)


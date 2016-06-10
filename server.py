from flask import Flask, render_template, request, flash, jsonify
from flask import redirect, url_for, session
from form import ContactForm
from IOT_Arduino import ArduinoControl
# If run on Raspberry Pi
 from IOT_RPi import RPiControl
#~ #celery task
#from tasks import temp_loop, count

app = Flask(__name__)
app.secret_key= 'waterscope'



# few variables initialise


@app.route("/IOT", methods = ['GET', 'POST'])
def contact():
	global serial_port
	global incubator
	global task
	
	# few variables initialise
	form =  ContactForm()
	if request.method == 'POST':	
	#Change default value once user input  something
		form.Port.default = form.Port.data
		form.port_command.default = form.port_command.data
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

		# Press Led_on/off button			
		elif 'led_button_on' in request.form:
			serial_port.excute('high')
			return render_template('index.html', form = form)
			
		elif 'led_button_off' in request.form:
			serial_port.excute('low')
			return render_template('index.html', form = form)


		elif 'set_sensor' in request.form:
			incubator = RPiControl(int(form.relay_pin.data), form.sensor_location.data,\
				float(form.Temperature.data))
			return render_template('index.html', form = form)
						
		# Press temperature change
		elif 'incubate' in request.form:
			incubator.set_pin()
			task = temp_loop.delay(1,incubator)
			return render_template('index.html', form = form)
			
		
		elif 'terminate' in request.form:
			task.revoke(terminate=True)
			return render_template('index.html', form = form)
			
			
		#~ # Press temperature change
		#~ elif 'incubate' in request.form:
			#~ incubator.set_pin()
			#~ task = count.delay(1)
			#~ return render_template('index.html', form = form)
			
		
		#~ elif 'terminate' in request.form:
			#~ task.revoke(terminate=True)
			#~ return render_template('index.html', form = form)
			
			
		#initialise the form
	elif request.method == 'GET':
		return render_template('index.html', form = form)
		
		


@app.route('/voltage')
def serial_monitor():
	global serial_port
	voltage = serial_port.monitor()
	return jsonify(voltage)
	


@app.route('/temperature')
def read_temperature():
	global incubator
	temperature = incubator.read_temp_json()
	return jsonify(temperature)


#~ @app.route('/incubator')
#~ def incubate():
	#~ global incubator
	#~ incubator.set_pin()
	#~ status = incubator.temp_control()
	#~ return jsonify(status)
	


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
	#app.run(host='10.0.0.1', debug=True)
#app.run(port=8000,debug=True)


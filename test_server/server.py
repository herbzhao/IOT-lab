from flask import Flask, render_template, request, flash, jsonify
from form import ContactForm
# If run on Raspberry Pi
 #~ from IOT_RPi import RPiControl
#celery task
#~ #from tasks import temp_loop, count

app = Flask(__name__)
app.secret_key= 'waterscope'



# few variables initialise


@app.route("/", methods = ['GET', 'POST'])
def contact():
	
	#~ # few variables initialise
	form =  ContactForm()
	#~ if request.method == 'POST':	
		#~ return render_template('index.html', form = form)

		
		#~ if 'set_serial' in request.form: 
			#~ # initialise Arduino serial port
			#~ serial_port = ArduinoControl(form.Port.data)
			#~ serial_port.set_serial()
			#~ # return to HTML page once submit
			#~ return render_template('index.html', form = form)
		
			
		
		#~ elif 'terminate' in request.form:
			#~ task.revoke(terminate=True)
			#~ return render_template('index.html', form = form)
			
			
		#~ #initialise the form
	#~ elif request.method == 'GET':
	return render_template('index.html', form = form)
		
		


#~ @app.route('/voltage')
#~ def serial_monitor():
	#~ global serial_port
	#~ voltage = serial_port.monitor()
	#~ return jsonify(voltage)
	



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
	#app.run(host='10.0.0.1', debug=True)
#app.run(port=8000,debug=True)


import serial
from flask import Flask, render_template, request, flash, jsonify, g, session
from flask import redirect, url_for
from IOT_Arduino import ArduinoControl
import time
import sqlite3
import gviz_api



app = Flask(__name__)
app.secret_key= 'waterscope'


# few variables initialise

	
#@app.teardown_request
#def teardown_request(exception):
#	g.status = False



@app.route('/')
def template():	
	return render_template('index.html')




serial_port = ArduinoControl('/dev/cu.wchusbserialfa140')
serial_port.set_serial()
@app.route('/voltage')
def query_data():
	
	global serial_port
	voltage = serial_port.voltmeter()
    
    # Prepare Data table description
	description = [("Label","string"),("Value","number")]
  

	# Prepare database value for data_table

    #format the data from database
	data = [["Voltage",voltage]]
		
	
	# Loading the description into the gviz_api.DataTable
	data_table = gviz_api.DataTable(description)
	
	# Loading the data into the gviz_api.DataTable
	data_table.LoadData(data)
	

	# Create a JSON responsse.
	json_data = data_table.ToJSon()

	return json_data




@app.route('/result')
def serial_monitor():
	
#	voltage = serial_port.monitor()
#	print voltage 
	return jsonify(voltage)

    
if __name__ == '__main__':
	app.run(debug=True)



import serial
from flask import Flask, render_template, request, flash, jsonify, g, session
from flask import redirect, url_for
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


@app.route('/database')
def query_data():
	
    # Prepare Data table description
	description = [("ID","number"),("Temp","number")]
  

	# Prepare database value for data_table

	#Open Sqlite database
	conn = sqlite3.connect('templog.sqlite')
	c = conn.cursor()  # create a cursor, so we can modify the database
    
    
    #Retrive data from database using SELECT
	c.execute("SELECT {idc}, {cn3} FROM {tn}"\
		.format (idc = 'index_column', cn3 = 'temperature', tn = 'tempearture_log' ))
		
    #format the data from database
	data = []
	rows = c.fetchall()
	for row in rows:
		row_data = [row[0],row[1]]
		data.append(row_data)
		
	#Close the cursor
	c.close()
	
	# Loading the description into the gviz_api.DataTable
	data_table = gviz_api.DataTable(description)
	
	# Loading the data into the gviz_api.DataTable
	data_table.LoadData(data)
	


	# Create a JSON responsse.
	json_data = data_table.ToJSon(columns_order=("ID", "Temp"), 
			order_by="ID")

	return json_data


    
if __name__ == '__main__':
	app.run(debug=True)



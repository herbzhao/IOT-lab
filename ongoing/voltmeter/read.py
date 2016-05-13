import serial
from flask import Flask, render_template, request, flash, jsonify, g, session
from flask import redirect, url_for
from IOT_Arduino import ArduinoControl
import time
import sqlite3
import gviz_api



serial_port = ArduinoControl('/dev/cu.wchusbserialfa140')
serial_port.set_serial()

def query_data():	
	global serial_port
	voltage = serial_port.voltmeter()
	return voltage

voltage = query_data()
description = [("Label","string"),("Value","number")]
data = [["Voltage",voltage]]

#print description
#print type(description)
print data
print type(data)


data_table = gviz_api.DataTable(description)	
	# Loading the data into the gviz_api.DataTable
data_table.LoadData(data)
	# Create a JSON responsse.
json_data = data_table.ToJSon(columns_order=("Label","Value"),
		order_by="Label")


print json_data


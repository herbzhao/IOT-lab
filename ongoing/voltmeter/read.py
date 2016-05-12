import serial
from flask import Flask, render_template, request, flash, jsonify, g, session
from flask import redirect, url_for
from IOT_Arduino import ArduinoControl
import time
import sqlite3
import gviz_api


@app.route('/')
def template():	
	return render_template('index.html')


@app.route('/database')
def query_data():
	
    # Prepare Data table description
	description = [("ID","number"),("Temp","number")]


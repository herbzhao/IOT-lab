
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
 
@app.route('/')
def interactive():
	return render_template('interactive.html')
	
	
	
@app.route('/background_process')
def background_process():
	try:
		lang = request.args.get('proglang', 0, type=str)
		if lang.lower() == 'python':
			return jsonify(result='You are wise')
		else:
			return jsonify(result='Try again.')
	except Exception as e:
		return str(e)
		
if __name__ == '__main__':
    app.run( debug=True)

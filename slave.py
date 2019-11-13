from flask import Flask, request, send_from_directory
import subprocess
import sys

app = Flask(__name__)

@app.route('/get/')
def run():
    try:
        repo = request.args.get('repo')
        subprocess.Popen(['scripts/slave-activate', str(repo)])
        return("Updating repository: " + repo + "\nSuccess!\n")
    except:
        return("Could not update " + repo + "\n")

@app.route('/')
def default():
    try:
        with open(str(sys.argv[1]), 'r') as file:
    	    contents = file.read()
    	    return(contents)
    except:
        return("Cannot serve " + str(sys.argv[1]))

app.run(host='0.0.0.0', debug=False, port=9999)

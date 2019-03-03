from flask import Flask, jsonify
from flask import request
import requests
import subprocess

host = "https://waketfup.org/api/events"
headers = {"Authorization" : "TESTAPIKEY"}
timeArry = []

def play_mp3(path):
    subprocess.Popen(['mpg123', '-q', path])

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def create_tasks():
    time = request.args.get('time')
    requests.post(host, headers=headers, data={"user_ID": 1, "timestamp": time})
    timeArry.append(time)
    if (len(timeArry) >= 5):
        play_mp3("sound.mp3")
        timeArry.clear()
    return jsonify({"Array" : timeArry}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

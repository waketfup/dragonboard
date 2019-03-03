from flask import Flask, jsonify
from flask import request
import subprocess

timeArry = []

def play_mp3(path):
    subprocess.Popen(['mpg123', '-q', path]).wait()

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def create_tasks():
    time = request.args.get('time')
    timeArry.append(time)
    if (len(timeArry) >= 5):
        play_mp3(sound.mp3)
        while (len(timeArry) > 0):
            timeArry.clear()
    return jsonify({"Array" : timeArry}), 200

if __name__ == '__main__':
    app.run(debug=True)

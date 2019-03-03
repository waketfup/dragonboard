import random
from flask import Flask, jsonify
from flask import request
import requests
import subprocess

host = "https://www.waketfup.org/api/events"
headers = {"Authorization" : "TESTAPIKEY"}
timeArry = []

def play_mp3(path):
    subprocess.Popen(['mpg123', '-q', path])


def get_user(name):
    r = requests.get("https://www.waketfup.org/api/user/" + name, headers=headers)
    return r.json()

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def create_tasks():
    time = request.args.get('time')
    requests.post(host, headers=headers, data={"user_ID": 2, "timestamp": time})
    timeArry.append(time)
    if (len(timeArry) == 1):
        print("User may be falling asleep.")
    if (len(timeArry) == 2):
        play_mp3("beep.mp3")
    if (len(timeArry) == 3):
        list = []
        list.append("rick_roll.mp3")
        list.append("sail.mp3")
        list.append("bring_me_to_life.mp3")
        play_mp3(random.choice(list))
        list.clear()
    if (len(timeArry) == 4):
        user = get_user("steve")
        print("Notifying the user's emergency contact(" + str(user["contact"]) +").")
        timeArry.clear()

    return jsonify({"Array" : timeArry}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

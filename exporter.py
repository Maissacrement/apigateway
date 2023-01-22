from dotenv import load_dotenv
from flask import Flask, Response
import docker
import json
import os

load_dotenv()

app = Flask(__name__)
client = docker.from_env()

def games():
    netName=os.environ.get('NETWORK_NAME') or 'luckyyou-game'
    e=client.networks.get(netName)
    gameList=[]
    for c in e.containers:
        for k in dict(c.attrs['NetworkSettings']['Networks']):
            if k == netName:
                gameList.append(json.dumps([c.name, c.attrs['NetworkSettings']['Networks'][k]['IPAddress']]))
    
    return json.dumps(gameList)


@app.route("/")
def hello_world():
    return Response(games(), mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host="0.0.0.0", port="5000")

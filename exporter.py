from dotenv import load_dotenv
from flask import Flask
import docker
import json
import os

load_dotenv()

app = Flask(__name__)
client = docker.from_env()

@app.route("/")
def hello_world():
    netName=os.environ.get('NETWORK_NAME') or 'luckyyou-game'
    e=client.networks.get(netName)
    game=[ [ c.attrs['NetworkSettings']['Networks'][k]['IPAddress'] for k in dict(c.attrs['NetworkSettings']['Networks']) if k == netName ] for c in e.containers ]
    return json.dumps(game)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host="0.0.0.0", port="5000")

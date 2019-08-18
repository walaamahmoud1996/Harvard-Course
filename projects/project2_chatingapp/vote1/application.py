import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit
from flask_jsglue import JSGlue
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

votes = {"yes": 0, "no": 0, "maybe": 0}
ava_channels = {"available_channels":[]}

jsglue = JSGlue(app)
@app.route("/")
def index():
    return render_template("index.html", votes=votes)

#
# @socketio.on("submit vote")
# def vote(data):
#     selection = data["selection"]
#     votes[selection] += 1
#     emit("vote totals", votes, broadcast=True)
@socketio.on('get channels',namespace='/channels')
def get_channels():
    emit('channel list',ava_channels)
@socketio.on('add channel',namespace='/channels')
def add_channel(data):
    print(data)
    ava_channels['available_channels'].append(data['channel_name'])
    emit('new channel',data['channel_name'],broadcast = True)


@app.route('/channels')
def channels():
    return render_template('channels.html')
@app.route('/channel/<string:channel_name>')
def channel(channel_name):
    return channel_name

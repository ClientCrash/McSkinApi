import requests
import json
import base64
from flask import Flask
app = Flask(__name__)



def getSkinUrlFromName(name: str):
    id_o = json.loads(requests.get(
        "https://api.mojang.com/users/profiles/minecraft/"+name).text)
    id = id_o['id']
    userinfo_t = requests.get(
        "https://sessionserver.mojang.com/session/minecraft/profile/"+id).text
    userinfo_o = json.loads(userinfo_t)
    props = json.loads(base64.b64decode(userinfo_o['properties'][0]['value']))
    skin_url = props['textures']['SKIN']['url']
    return skin_url

@app.route("/")
def home():
    return "<h1 style='font-family:Arial'>Index</h1><br/><small><a href='https://github.com/clientcrash'>Github</a></small>"

@app.route("/url/<name>")
def urlPage(name):
    return getSkinUrlFromName(name)

if __name__=="__main__":
    app.run()
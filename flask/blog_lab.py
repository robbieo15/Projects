from re import template
from unicodedata import name
from flask import Flask, render_template
app = Flask(__name__)

blogs = [
    {'title': "NASA Verifies Minerals on Sun",
    'author': "A Yeti",
    'date': "September 16th, 2022",
    'body': "You wouldn't believe what they actually found on the dang ol' sun. Minerals. Heard it hear first. Life might be on the Sun. Supposedly, after compiling data from the layer beneath the flamey surface, they found life was once on the Sun. These minerals may lead us to know more about the shiny star.",
    'url': "http://127.0.0.1:5000/blog1",
    'key': '1'
    },
    {'title': "First Martian Claims Central Citizenship",
    'author': "A Yeti",
    'date': "September 16th, 2022",
    'body': "Central Land has accepted a Martian as a citizen. The threat to the rest of us is unfathomable. We must allow these Martians into our land as soon as possible. Since the latest martian ban, our tech industries have plummeted and we're missing general workers. There's no reason to bar them from entry. Central Land's GDP is exploding because of this alone.",
    'url': "http://127.0.0.1:5000/blog2",
    'key': '2'
    },
    {'title': "Call Of Duty VR or Gun Gale Reality",
    'author': "A Yeti",
    'date': "September 16th, 2022",
    'body': "Call of Duty's latest game has left several people dead. A mod was created called one in a chamber where a player receives an electral shock large enough to cause a heart attack. Some have survived the mod, but most have not.",
    'url': "http://127.0.0.1:5000/blog3",
    'key': '3'
    },
    {'title': "Who Murdered My Pet Rock",
    'author': "A Yeti",
    'date': "September 16th, 2022",
    'body': "MY PET ROCK!!!! WHAT HAPPENED! i'm just using this to vent but my pet rock has become gravel. Was it the neighbor? John McAffe... Please Send any information you have to me.",
    'url': "http://127.0.0.1:5000/blog4",
    'key': '4'
    }
]

@app.route('/')
def index():
    return render_template("index.html",blogs=blogs)

@app.route('/blog1')
def blog1():
    return render_template("blog1.html",blogs=blogs)

@app.route('/blog2')
def blog2():
    return render_template("blog2.html",blogs=blogs)

@app.route('/blog3')
def blog3():
    return render_template("blog3.html",blogs=blogs)

@app.route('/blog4')
def blog4():
    return render_template("blog3.html",blogs=blogs)
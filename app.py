from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World, this is python gitlab demo project"


app.run(host="0.0.0.0" , port=80)
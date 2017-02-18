from flask import *
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Alexa and Chris are getting married!</h1>"

@app.route("/index")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
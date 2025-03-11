from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Study Buddy On Top'


if __name__ == "__main__":
    app.run()

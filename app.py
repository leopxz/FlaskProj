from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
    return "ola"

@app.route("/teste")
def teste():
    return "olax"

if __name__ == "__main__":
    app.run()

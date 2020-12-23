from flask import Flask
app = Flask (__name__)

@app.route('/')
def GAE():
    return "<h2>The web application was launched successfully using GAE</h2>"

if __name__ == "__main__":
    app.run()

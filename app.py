from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")

def welcome():
    html = "Hello {hostname} & Welcome!" 
    return html.format(hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
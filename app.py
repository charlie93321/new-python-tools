import base64
from random import Random

from flask import Flask, send_from_directory
app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")
@app.route('/')
def hello_world():
      return "hello"





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)

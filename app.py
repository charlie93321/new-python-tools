import base64
from random import Random
import com.dxm.flask_web.i18nLangApp
from flask import Flask, send_from_directory
app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")
@app.route('/')
def hello_world():
      return "hello"

from com.dxm.flask_web.i18nLangApp import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)

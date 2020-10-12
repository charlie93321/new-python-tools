import base64
from random import Random
import com.dxm.flask_web.i18nLangApp
from flask import Flask, send_from_directory
app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")

@app.route('/2')
def hello_world2():
      return "hello2"
import base64
from random import Random
import com.dxm.flask_web.i18nLangApp
from flask import Flask, send_from_directory

from app import app

@app.route('/i18n')
def i18n_pages():
    return app.send_static_file('pages/htmls/i18n.html')

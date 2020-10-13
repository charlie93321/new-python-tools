import base64
import json
from random import Random

from redis import StrictRedis

import com.dxm.flask_web.i18nLangApp
from flask import Flask, send_from_directory, request

from app import app
redisContext = {'cli':None}

@app.route('/i18n')
def i18n_pages():
    return app.send_static_file('pages/htmls/i18n.html')

@app.route('/i18n/keys')
def i18n_keys():

    if redisContext['cli'] is None:
        redisContext['cli'] = StrictRedis(host='124.70.208.68', port=6379, db=1, password='hadoop')

    ps=request.args
    rs=''
    if ps.has_key('pattern'):
        rs = redisContext['cli'].keys(ps['pattern'])
    else:
        rs= redisContext['cli'].keys('*')
    objs={}
    if  len(rs)>0:
        for key in rs:
            value = redisContext['cli'].get(key)
            objs[key]=value
    return json.dumps({'data':objs})

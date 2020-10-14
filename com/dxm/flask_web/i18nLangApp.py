import json

from flask import request
from redis import StrictRedis

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
    objs=[]
    if  len(rs)>0:
        for key in rs:
            value = json.loads(redisContext['cli'].get(key),encoding='utf-8')
            entity = {"key":key,"zh":value['zh'],"en":value['en'],"version":value['version'],"desc":value['desc']}
            objs.append(entity)
    return json.dumps({'list':objs})


#delKey
@app.route('/i18n/delKey')
def i18n_delKey():
    if redisContext['cli'] is None:
        redisContext['cli'] = StrictRedis(host='124.70.208.68', port=6379, db=1, password='hadoop')
    ps=request.args
    if ps.has_key('key'):
        redisContext['cli'].delete(ps['key'])
    return json.dumps({"code":0})

@app.route('/i18n/update',methods = ["POST"])
def i18n_update():
    if redisContext['cli'] is None:
        redisContext['cli'] = StrictRedis(host='124.70.208.68', port=6379, db=1, password='hadoop')
    data=json.loads(request.data,encoding='utf-8')
    redisContext['cli'].set(data['key'],request.data)
    return json.dumps({"code":0})

@app.route('/i18n/save',methods = ["POST"])
def i18n_save():
    if redisContext['cli'] is None:
        redisContext['cli'] = StrictRedis(host='124.70.208.68', port=6379, db=1, password='hadoop')
    data = json.loads(request.data, encoding='utf-8')
    rs = redisContext['cli'].get(data['key'])
    if rs is None:
        redisContext['cli'].set(data['key'], request.data)
        return json.dumps({"code": 0})
    if rs is not None:
        return json.dumps({"code":1})
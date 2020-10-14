import gzip
import json
import os
from StringIO import StringIO

from datetime import datetime

from flask import request, send_from_directory, send_file
from pathlib import Path
from redis import StrictRedis

from app import app


def gzip_compress(buf):
    out = StringIO()
    with gzip.GzipFile(fileobj=out, mode="w") as f:
        f.write(buf)
    return out.getvalue()


def gzip_decompress(buf):
    obj = StringIO(buf)
    with gzip.GzipFile(fileobj=obj) as f:
        result = f.read()
    return result


redisContext = {'cli': None}


def is_empty(string):
    if string is None:
        return True
    if len(string.strip()) == 0:
        return True
    return False


def has_and_not_empty(args, key):
    if args.has_key(key):
        if not is_empty(args[key]):
            return True
    return False


@app.route('/sql')
def sql_pages():
    return app.send_static_file('pages/htmls/sql.html')


@app.route('/sql/search')
def sql_search():
    if redisContext['cli'] is None:
        redisContext['cli'] = StrictRedis(host='124.70.208.68', port=6379, db=2, password='hadoop')

    args = request.args
    key = None
    desc = None
    date = None
    keys = ''
    if has_and_not_empty(args, 'key'):
        key = args['key'].strip()

    if has_and_not_empty(args, 'desc'):
        key = args['desc'].strip()

    if has_and_not_empty(args, 'date'):
        key = args['date'].strip()

    if key is None:
        keys = redisContext['cli'].keys()
    else:
        keys = redisContext['cli'].keys(key)
    objs = []
    if len(keys) > 0:
        for key in keys:
            value = redisContext['cli'].get(key)
            if not is_empty(value):
                obj = json.loads(gzip_decompress(value), encoding='utf-8')
                is_add = True
                if desc is not None:
                    if desc not in obj['desc']:
                        is_add = False
                if date is not None:
                    if date not in obj['date']:
                        is_add = False
                if is_add:
                    objs.append(obj)

    return json.dumps({"list": objs}, ensure_ascii=False)


@app.route("/sql/download")
def sql_download():
    dateStr = datetime.strftime(datetime.now(), '%Y/%m/%d')
    if redisContext['cli'] is None:
        redisContext['cli'] = StrictRedis(host='124.70.208.68', port=6379, db=2, password='hadoop')

    key = request.args['key'].strip()
    value = redisContext['cli'].get(key)

    dir = "static/sql/{}".format(dateStr)

    sql_dir = Path(dir)
    if not sql_dir.exists():
        print sql_dir.absolute()
        os.makedirs(dir)

    with open(dir + "/{}.sql".format(key), 'w') as f:
        newData = json.loads(gzip_decompress(value), encoding='utf-8')
        f.write(gzip_decompress(newData['content']))
    return json.dumps({'path': dir + "/{}.sql".format(key)}, ensure_ascii=False)

# encoding=utf-8
import gzip
import json
from StringIO import StringIO

import redis
from redis import StrictRedis

lines = '''


select id,name
from t_ship_print_template_style
where channel_id = 167 ;

select *
from t_ship_print_template_size
where template_style_id in (90, 93);



update t_ship_print_template_style ts
set ts.img= 'https://album.bigseller.com/static/template/printimg/0abc368aaafc124975787c6d6ab8d6cd.jpg',
    ts.thumbnail='https://album.bigseller.com/static/template/printimg/ef1de3d4a8dd8ad0dbd1bc2488eb3524.jpg',
    ts.update_time=sysdate()
where channel_id = 167
  and id = 90;



INSERT INTO t_ship_print_template_style (channel_id, name, lang_key, type, img, thumbnail, is_default)
VALUES (167, 'Label With Product Info', 'ship.config.label.template.with.product', 1,
        'https://album.bigseller.com/static/template/printimg/101f47a941b73c1f0a2f7b25ec8a2908.jpg',
        'https://album.bigseller.com/static/template/printimg/833f866accc29ad0a5db6a870755e8db.jpg', 0);




INSERT INTO erp_id.t_ship_print_template_size (template_style_id, size, lang_key, size_source, additional_type, url,
                                               is_senderInfo)
VALUES (93, '100*150mm', 'ship.config.label.template.size.thermal.fifteen', 1, 1, '/10x15/label/shopee-express-my_15.ftl',
        1);
'''


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


redis = StrictRedis(host='124.70.208.68', port=6379, db=2, password='hadoop')

# redis.set(name='shopee-my-express-online-sql-gzip',value=gzip_compress(lines))

# print len(gzip_decompress(redis.get('shopee-my-express-online-sql-zip')))
# print len(redis.get('shopee-my-express-online-sql-gzip'))
data = {
    "key": "sql.poslaju.qrcode",
    "content":gzip_compress(lines),"desc":"qr code 识别",
    "date":'2020-10-14'
}

redis.set(name='sql.poslaju.qrcode', value=json.dumps(data, ensure_ascii=False))
print  redis.get('sql.poslaju.qrcode')


redis.close()

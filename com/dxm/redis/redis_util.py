import redis
from redis import StrictRedis

lines = '''
select * from t_ship_print_template_style where channel_id=167;

update t_ship_print_template_style ts
set ts.img= 'https://album.bigseller.com/static/template/printimg/c2142afc843f991fa2061a7b6c8a4fb7.jpg',
    ts.thumbnail='https://album.bigseller.com/static/template/printimg/71d9ded90108c9a7430db97d089a58a6.jpg',
    ts.update_time=sysdate()
where channel_id = 167 and id=90;

INSERT INTO t_ship_print_template_style (channel_id, name, lang_key, type, img, thumbnail, is_default)
VALUES (167, 'Label With Product Info', 'ship.config.label.template.with.product', 1,
        'https://album.bigseller.com/static/template/printimg/2806d9b5f168dc02d839ac1112613721.jpg',
        'https://album.bigseller.com/static/template/printimg/e3fbdf6df729ba4e45b1cbd26c097df3.jpg', 0);



select * from t_ship_print_template_size where template_style_id in(90,93);

INSERT INTO erp_id.t_ship_print_template_size (template_style_id, size, lang_key, size_source, additional_type,
                                               url, is_senderInfo)
VALUES (93, '100*150mm', 'ship.config.label.template.size.thermal.fifteen', 1, 1,
        '/10x15/label/shopee-je-my_15.ftl', 1);
'''

redis = StrictRedis(host='124.70.208.68', port=6379, db=0, password='hadoop')

print(redis.set(name='shopee-my-express-online-sql',value=lines))

print redis.get('shopee-my-express-online-sql')
redis.close()
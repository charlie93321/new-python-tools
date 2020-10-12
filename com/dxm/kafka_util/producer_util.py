#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='124.70.208.68:9092')



msg = "Hello World".encode('utf-8')  # 发送内容,必须是bytes类型

producer.send('test-zxy', msg)  # 发送的topic为test
producer.close()

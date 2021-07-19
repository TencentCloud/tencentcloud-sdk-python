# -*- coding:utf-8 -*-
import sys
import time
import json
import random
import string
import cls_kv_pb2

##pb协议客户自定义
def pb_gen(start_index, size):
    logGroupList = cls_kv_pb2.LogGroupList()
    LogGroup = logGroupList.logGroupList.add()
    log = LogGroup.logs.add()
    log.time = int(time.time())
    for index in range(size):
        content = log.contents.add()
        key = "name,index,test_name_index,"
        content.key = key + ''.join(random.sample(string.ascii_letters + string.digits, 60))
        value = "test_" + str(start_index) + "_" + str(index) + "_"
        for i in range(2):
            content.value = content.value + ''.join(random.sample(string.ascii_letters + string.digits, 60))
    data = logGroupList.SerializeToString()

    return data


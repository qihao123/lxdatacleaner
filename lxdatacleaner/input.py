# -*- coding: utf-8 -*-
import pandas as pd
import sqlalchemy as sql
from pykafka import KafkaClient
import json

import csv
'''
@author:Hao Qi

@version:0.0.1
'''
"""
Copyright © 2020 <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the “Software”), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# 数据输入类，读取各形式的数据，返回pandas形式的数据对象，DataFrame


class input(object):
    #输入csv格式数据
    @staticmethod
    def read_csv(filepath: str, encoding: str):
        # pandas读取csv文件返回DataFrame对象
        try:
            file = pd.read_csv(filepath, encoding=encoding)
            return file
        except:
            # 读取错误打印读取错误信息，返回空DataFrame
            print("csv file open error")
            file = pd.DataFrame()
            return file
    #输入mysql数据库格式数据
    def read_database(self, host: str,port: str, user: str, password: str, database: str, table: str):
        try:
            con = self.__get_con(host,user,password,port,database)
            table = pd.read_sql_table(table,con)
            return table
        except:
            print('connect database error')
            df = pd.DataFrame()
            return df
    #输入kafka数据（流式数据，接收json格式数据）输出csv文件，以追加数据的方式输出数据
    def read_kafka(self, kfk_host, zk_host,topic,save_path):
        #host = '192.168.10.217:9092'
        #zk_host='192.168.10.217:2181'
        client = KafkaClient(hosts=kfk_host, zookeeper_hosts=zk_host)
        print(client.topics)
        # 消费者
        #topic='messagetest'
        global flag
        flag=1
        topic = client.topics[topic.encode()]
        consumer = topic.get_simple_consumer(consumer_group=b'test_group', auto_commit_enable=True,
                                             auto_commit_interval_ms=1,
                                             consumer_id=b'test_id')
        for message in consumer:
            if message is not None:
                #json2csv
                #json = message.value.decode('utf-8')
                print(message.offset, str(eval(message.value.decode('utf-8'))).replace("'",'"'))
                self.__writerow(str(eval(message.value.decode('utf-8'))).replace("'",'"'),save_path,flag)
                flag=2
                #print(message.offset, message.value.decode('utf-8'))

    #获取数据库链接方法，外部不可访问

    def __get_con(self,host,user,password,port,database):
        connect_url='mysql+pymysql://'+user+':'+password+'@'+host+':'+port+'/'+database
        #connection = sql.engine.create_engine('mysql+pymysql://crawl:123456@192.168.10.155:3306/')
        connection = sql.engine.create_engine(connect_url)
        con = connection.connect()
        return con
    #json2csv,json文件转csv文件，追加写入
    def __writerow(self,jsons,csv_path,flag):
        #json_file = json.dumps(jsons)
        csv_file = open(csv_path, 'a', newline='', encoding='utf8')
        writer = csv.writer(csv_file)
        # 读取json数据
        dic_data = json.loads(jsons)

        keys = []
        for dic in dic_data:
            keys.append(dic)
            #keys = dic.keys()
        # 写入列名,flag为True写入列名，为false则不写入

        if (flag==1):
            writer.writerow(keys)
            flag+=1

            #break
        data=[]
        for dic in dic_data:
            for key in keys:
                data.append(str(dic_data[key]))
                if key not in dic:
                    data.append('')

            #writer.writerow(dic.values())
        writer.writerow(data)
        csv_file.close()


if __name__ == '__main__':
    input = input()
    #table = input.read_database('192.168.10.155','3306','crawl','123456','mysql','user')
    #print(table.head())
    #import json
    #jsons = { "name":"AAA" , "age":"17" },{ "name":"BBB" , "age":"18" },{ "name":"CCC" , "age":"19" }
    #csv_path='D:\\project\\dataclean\\test\\d.csv'
    #input.read_kafka('192.168.10.217:9092','192.168.10.217:2181','messagetest',csv_path)




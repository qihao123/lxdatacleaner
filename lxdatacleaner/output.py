# -*- coding: utf-8 -*-
import pandas as pd
import sqlalchemy as sql

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


# 数据输出类，输出各形式的数据，写入数据到文件系统或消息队列或数据库中

class output(object):

    def to_csv(self,df,path,encoding):
        try:
            df.to_csv(path,encoding=encoding)
            print("successed save file to %s",path)
        except:
            print("save file error")

    def to_mysql(self,df,tablename,databasename,host,port,user,password):
        try:
            con = self.__get_con(host,user,password,port,databasename)
            df.to_sql(name=tablename,con=con)
            print('save to mysql successed')
        except:
            print('save to mysql has error')


    def to_json(self,df):
        try:
            res = df.to_json()
            return res
        except:
            print('to json error')
            df = pd.DataFrame()
            return df

    def __get_con(self,host,user,password,port,database):
        connect_url='mysql+pymysql://'+user+':'+password+'@'+host+':'+port+'/'+database
        #connection = sql.engine.create_engine('mysql+pymysql://crawl:123456@192.168.10.155:3306/')
        connection = sql.engine.create_engine(connect_url)
        con = connection.connect()
        return con

if __name__ == '__main__':

    df = pd.read_csv('D:\\project\\dataclean\\test\\a.csv',encoding='utf-8')

    #print(df.head())
    output=output()
    #output.to_mysql(df,'test','test2','192.168.10.155','3306','crawl','123456')
    #print(output.to_json(df))
# -*- coding: utf-8 -*-
import pandas as pd

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


# 数据定义域类，输入数据，输出是否在该定义域中
class domain(object):

    def between(self,df,column,low: float,top: float):
        try:
            df = df[df[column]>=low & df[column]<=top]
            return df
        except:
            print('This domain option error')
            df=pd.DataFrame()
            return df
        

    def not_between(self,df,column,low: float,top: float):
        try:
            df = df[df[column]<=low&df[column]>=top]
            return df
        except:
            print('This domain option error')
            df=pd.DataFrame()
            return df
        

    def in_domain(self,df,column,list):
        try:
            df = df[df[column].isin(list)]
            return df
        except:
            print('This domain option error')
            df=pd.DataFrame()
            return df


    def out_domain(self,df,column,list):
        try:
            df = df[df[column].notin(list)]
            return df
        except:
            print('This domain option error')
            df=pd.DataFrame()
            return df

# -*- coding: utf-8 -*-
import pandas as pd
import queue
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
#时间所限，0.0.1版本暂不实现flow功能
class flow(object):
    def append(self):
        append()
    def __init__(self):
        self.q=queue.Queue()
        self.flow_name=''
        self.index=[]
        self.options=[]
        self.args=[]
        self.data=[]

    def create_flow(self,flow_name: str,):
        self.flow_name=flow_name


    def delete_work(self):
        pass
    def print_flow(self):
        pass
    def updata_work(self):
        pass
    def run_work(self):
        pass
class append(flow):
    def append_input_work(self,options,df,colunm):
        self.index.append(max(self.index)+1)

        pass
    def append_domain_work(self):
        pass
    def append_check_work(self):
        pass
    def append_output_work(self):
        pass


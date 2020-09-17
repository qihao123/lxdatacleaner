import lxdatacleaner as dc
import pandas as pd
'''
input = dc.input()

path = 'D:\\project\\dataclean\\test\\b.csv'
a = input.read_csv('D:\\project\\dataclean\\test\\b.csv', 'utf-8')
# print(a.head())
ll = ['轮式拖拉机']
domain = dc.domain()
b = domain.in_domain(df=a, column='jizhong', list=ll)
print(b.head())
output = dc.output()
#output.to_csv(b, path, 'utf-8')
check = dc.check()

c = check.check_Phonenum(b,'jixing')
print(c[c['PhoneNumber_check']==True].head())
check.check_address.check_sheng(a,'zhong')
'''
a="{'id': '11', 'sheng': '安徽省', 'shi': '六安市', 'xian': '霍邱县', 'zhen': '高塘镇', 'cun': '八里村赵店组', 'name': '曾凡明', 'jijupinmu': '自走履带式谷物联合收割机（全喂入）', 'shengchanchangjia': '星光农机股份有限公司', 'chanpinmingcheng': '全喂入联合收割机', 'goumaijixing': '4LZ-5.0Z', 'goumaishuliang': '1', 'jingxiaoshang': '霍邱县承军商贸有限公司(经销商)', 'date': '43733', 'dantaishoujia': '100000.0', 'dantaibutie': '28000', 'butiezonge': '28000.0', 'zhuangtai': '已提交财政部门未结算', 'jizhong': '全喂入收割机', 'jixingfenlei': '5≤喂入量＜6kg/s'}"
import json
#print(a.replace(",",'"'))
b = json.loads(a.replace("'",'"'))
print(b)
keys = []

for dic in b:
    keys.append(dic)
    #print(dic)
    #print(b[dic])
    print(keys)
print(keys)
    #keys = dic.keys()
    #print(keys)
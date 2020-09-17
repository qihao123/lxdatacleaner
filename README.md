# lxkjdatacleaner 数据清洗库
公司内部自用的python数据清洗库
## 主要功能
- 数据字段清洗，各字段类型校验与强制转换
- 数据删除与填充
- 数据字段中，域的定义
- 流式数据校验，清洗
## 数据输入输出
- 支持输入输出文本文件，csv格式输入输出
- 支持输入输出数据库，mysql，MariaDB
- 支持输入消息队列，KAFKA
- 仅支持输出：json
- 根据如上输入输出规则可自定义输入输出
## 安装
```
pip install lxkjdatacleaner
```
## 使用
```
import lxkjdatacleaner as lxdc
#输入,首先进行实例化，然后调用函数
input = lxdc.input()
domain = lxdc.domain()
check = lxdc.check()
output = lxdc.output()

#文件位置，目前仅支持绝对位置
path = 'D:\\project\\dataclean\\test\\xxx.csv'

#数据输入，目前支持输入csv文件，返回pandas.core.Dataframe对象
a = input.read_csv(path, 'utf-8')

#数据域判断，输入DataFrame，列名，域列表（字符串型）或域范围（数字），返回DataFrame，后买你追加Boolean类型列，判断值是否在域中
name = ['李明'，’张三‘]
b = domain.in_domain(df=a, column='name', list=name)
c = domain.between(df=a,column='age',low=0.0,top=14.0)
#out_domain,not_between同理

#值校验
#校验电话号，新增Boolean类型的列，校验电话号码的正确性，0.0.1版本支持，电话，邮箱，省名，市名的校验
c = check.check_Phonenum(b,'pnone_number')

#输出，该版本支持csv，mysql，json格式输出
output.to_csv(c, path, 'utf-8')
```

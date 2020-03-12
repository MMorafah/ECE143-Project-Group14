import re
import json
import requests
import xlwt
def requests_web_data(url):
    try:
        headers = {"User-Agent": "", "Cookie": ""}
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print(url)
        print('requests error!')
    else:
        return r.content
import codecs

f = codecs.open('time_id.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8’编码读取
line = f.readline()   # 以行的形式进行读取文件
list1 = []
while line:
    a = line.split()
    b = a   # 这是选取需要读取的位数
    list1.append(b)  # 将其添加在列表之中
    line = f.readline()
f.close()
time_ids=[]

for i in list1:
    time_ids.append(i[0])
for time_id in range(len(time_ids)):
    historical_data_url = 'https://www.eecso.com/test/weibo/apis/currentitems.php?timeid=' + str(time_ids[time_id])
    try:
        data = json.loads(requests_web_data(historical_data_url).decode('gb2312'))
        book = xlwt.Workbook()  # 创建一个Excel
        sheet1 = book.add_sheet('1')  # 在其中创建一个名为hello的sheet
        for i in range(len(data)):
            sheet1.write(i, 0, data[i][0])  # 往sheet里第一行第一列写一个数据
            sheet1.write(i, 1, data[i][1])
            sheet1.write(i, 2, data[i][2])
            sheet1.write(i, 3, data[i][3])
        book.save('data_day_'+str(time_id+1)+'.xls')  # 创建保存文件
    except:
        print(-1)
    else:
        print(time_id+1)

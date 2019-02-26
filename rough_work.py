import csv
import requests
from datetime import datetime, date
import time, re

current_time = str(datetime.time(datetime.now()))
print(current_time)

if re.match(r'^12\:3\d\:',current_time) or re.match(r'^12\:41\:',current_time):
    print('yes')
else:
    print('no')

'''list1 = '11/February/2019|3297.00|26376.00|3150.00|25200.00'
list2 = '11/February/2019|3297.00|26376.00|3150.00|25200.00'

with open ('result.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"')
    for val in csv_reader:
        lst_data = '|'.join(val)

#print(lst_data[:50])
#list2=lst_data[:50]

print(id(list1))
print(id(list2))


if list1 == list2:
    print('yes')
else:
    print('no')'''

'''
my_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
if 'abc-456' in my_list:
#if any('1234' in s for s in my_list):
    print('yes')'''

'''def get_content(url,method):
    content = getattr(requests,method)
    print(content(url))
    print(content(url).text)

get_content('http://www.livechennai.com/gold_silverrate.asp','get')'''


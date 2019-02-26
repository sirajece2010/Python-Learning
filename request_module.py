import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
import time
import csv
import smtplib
import config

first_flag = True
current_date = datetime.date(datetime.now())

def send_mail(subject,content):
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login(config.from_mail,config.mail_passwd)
    headers = [
        "From: " + config.from_mail,
        "Subject: " + subject,
        "To: " + config.to_mail,
        "MIME-Version: 1.0",
        "Content-Type: text/html"]
    headers = "\r\n".join(headers)
    mail.sendmail(config.from_mail,config.to_mail,headers + "\r\n\r\n" + content)
    mail.close()
    

while True:
    today = str(date.today())
    if first_flag:
        print('first if')
        first_flag = False
        content = requests.get('http://www.livechennai.com/gold_silverrate.asp').text
        soup = BeautifulSoup(content, 'lxml')
        b = soup.find_all('table', class_='table-price')

        for i in range(49,0,-5):
            date_ = str(b[1].find_all('td', class_='content')[i-4].text).strip()
            k24rate1 = str(b[1].find_all('td', class_='content')[i-3].text).strip()
            k24rate8 = str(b[1].find_all('td', class_='content')[i-2].text).strip()
            k22rate1 = str(b[1].find_all('td', class_='content')[i-1].text).strip()
            k22rate8 = str(b[1].find_all('td', class_='content')[i].text).strip()
            current_time = datetime.time(datetime.now())
            my_list = [date_, k24rate1, k24rate8, k22rate1, k22rate8, current_date, current_time]

            with open('result.csv', 'a+') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(my_list)

    elif (str(current_date) not in today):
        print('first elif')
        content = requests.get('http://www.livechennai.com/gold_silverrate.asp').text
        soup = BeautifulSoup(content, 'lxml')

        a = soup.find('table')
        b = soup.find_all('table', class_='table-price')
        date_ = str(b[1].find_all('font')[0].text).strip()
        k24rate1 = str(b[1].find_all('font')[1].text).strip()
        k24rate8= str(b[1].find_all('font')[2].text).strip()
        k22rate1 = str(b[1].find_all('font')[3].text).strip()
        k22rate8 = str(b[1].find_all('font')[4].text).strip()
        #print(type(a))c
        current_time=datetime.time(datetime.now())
        my_list = [date_,k24rate1,k24rate8,k22rate1,k22rate8,current_date,current_time]
        print(my_list)
        body = today + '=>' + k22rate1 + ' ' + k22rate8
        send_mail("Today's_Gold_Rate", body)

        fh = open('output_{}.html'.format(current_date), 'w')
        fh.write(a.encode('utf-8'))
        fh.close()

        with open('result.csv', 'a+') as csv_file:
            writer=csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(my_list)
    else:
        print ('Script started on {} and today is {}'.format(current_date,today))
        time.sleep(60*60*12)





'''f = codecs.open('output.txt', mode="w", encoding="iso-8859-1")
f.write(content.encode("iso-8859-1", "replace"))
f.close()'''



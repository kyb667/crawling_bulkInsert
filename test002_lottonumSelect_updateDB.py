import psycopg2
from psycopg2 import extras
from selenium import webdriver
import json

conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()

browser = webdriver.Chrome('-------file name--------------')

input_data = []
for i in range(10,923):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={0}'.format(i)
    browser.get(url)
    a = browser.find_element_by_tag_name('body')
    string = json.loads(a.text)
    data = []
    for i, j in string.items() :
        data.append(j)
    selectData = (data[2], data[10], data[13], data[11], data[12], data[5], data[7], data[4], data[9], data[6], data[8], data[3], data[0])
    input_data.append(selectData)

extras.execute_values(cur, "insert into lotto values %s", input_data)
conn.commit()
conn.close()

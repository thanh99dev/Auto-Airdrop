import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from datetime import date
import json







# Header
header = {
    "accept": 'text/html, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '641',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://ethereumshanghai.com',
    'referer': 'https://ethereumshanghai.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-kl-ajax-request': 'Ajax_Request',
    'x-requested-with': 'XMLHttpRequest'
}

# Time
today = date.today()
day = today.day
year = today.year
now1 = datetime.now()
timenow1 = now1.strftime("%d/%m/%Y, %H:%M:%S")
f = open('log.txt',"a")
f.write('\n-------------------------------------------------------------------\nMission starts at ' + str(timenow1))
f.close()

# Variable & Function
url = 'https://ethereumshanghai.com/airdrop/submit'

data1 = {'address': 0xf04aaE0981d01daf2d2F57E9162e6c8399668796}
 

def read_file(a):
    try:
            file = open(a, encoding='utf-8')
    except FileNotFoundError:
         file = open(a, "a+", encoding='utf-8')
    sst = file.read()
    return sst

def write_file(a,b):
        file = open(a, 'w', encoding='utf-8')
        file.write(b)
        file.close()

def add_file(file, text):
    tk = read_file(file)
    if tk =="":
        tk = text
        write_file(file, tk)
    else:
        tk = tk + '\n'+ text
        write_file(file, tk)

#  Execute
submit1 = requests.post(url,headers=header,data=data1)
print(submit1.status_code)
print(submit1.text)

# //*[@id="airdrop-form"]/div[2]/div
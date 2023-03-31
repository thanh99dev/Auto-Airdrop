from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import secrets
from eth_account import Account
from datetime import datetime
from datetime import date
import time



# Var

ref = 'https://blursea.io/'
# webrd = 'https://vanity-eth.tk/'
ii = 1
h = 0
check0 = '#withdraw'
check1 = '//*[@id="airdrop-form"]/div/input'
check2 = '//*[@id="airdrop-form"]/div/button'
check3 = '//*[@id="airdrop-block"]/div/div[1]/span[2]'
check4 = '//*[@id="airdrop-form"]/div/input'
check5 = '//*[@id="airdrop-form"]/div/button'
# Time
today = date.today()
day = today.day
year = today.year
now1 = datetime.now()
timenow1 = now1.strftime("%d/%m/%Y, %H:%M:%S")
f = open('log.txt',"a")
f.write('\n-------------------------------------------------------------------\nMission starts at ' + str(timenow1))
f.close()

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

# Auto programming

with open('data.csv') as f:
    reader = csv.reader(f,delimiter='|')
    l = [row for row in reader]
    with open("data.csv") as f:
        reader = csv.reader(f)
        for i in reader:
            swap = l[h][1]
            swap2 = l[h][0]
            print(swap)
            print(swap2)

            print("Dang Auto Cho Wallet: ",swap)
            h += 1
            time.sleep(1)
            driver = webdriver.Chrome(executable_path="C:/Users/lehuy/Documents/cd/chromedriver.exe")
            driver.get(ref)
            time.sleep(1)
            print('ok 1')
            cs1 = driver.find_element(By.XPATH,check1)
            cs1.send_keys(swap)
            time.sleep(1)
            ip2 = driver.find_element(By.XPATH, check5)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", ip2)
            time.sleep(2)
            ii1 = driver.find_element(By.CSS_SELECTOR,'#airdrop-block > div.col-12.col-sm-10.col-md-9.col-lg-8 > div.row.mt-4.text-center.justify-content-between > div:nth-child(2) > div.heading-h5.text-primary')
            print(ii1.text)
            iiok = 50 - int((ii1.text))
            print(iiok)
            ii11 = ii1.text
            
            if int(ii1.text) == 50:
                 okwd = driver.find_element(By.CSS_SELECTOR, check0)
                 driver.execute_script("arguments[0].click();", okwd)

                 print('Da Click Withdraw!!!')
            time.sleep(2)
           
            
            refok = driver.find_element(By.CSS_SELECTOR,'#airdrop-block > div > div.text-break > span.text-primary.copy')
            print("ok2")
            time.sleep(1)
            for ii in range(iiok):
                key = "0x" + secrets.token_hex(32)
                address = Account.from_key(key).address

                print('Address: ' + str(address) + '|' + str(key))
                add_file('wallet.txt',key+'|'+address)

                driver = webdriver.Chrome(executable_path="C:/Users/lehuy/Documents/cd/chromedriver.exe")
                driver.get(refok.text) 
                time.sleep(1)

                ip = driver.find_element(By.XPATH, check4)
                ip.send_keys(address)
                time.sleep(1)
                ip3 = driver.find_element(By.XPATH, check5)
                driver.execute_script("arguments[0].click();", ip3)
                time.sleep(2)
                print("Dang Auto Lan Thu " + str(ii) + " Cho Wallet:" + str(swap))
                #  Report Result
            time.sleep(1)
            print('ok 3')
            time.sleep(3)
            now2 = datetime.now()
            timenow2 = now2.strftime("%d/%m/%Y, %H:%M:%S")
            if ii == iiok:
                f = open('log.txt',"a")
                f.write('\n'+str(ii11) +' With ADDRESS : ' + str(swap) + '|' + str(swap2) + '\n At Time: ' + str(timenow2))
                f.close()
            else:
                f = open('log.txt',"a")
                f.write('\n' + str(ii11)+ ' With ADDRESS : ' + str(swap) + '|' + str(swap2) + '\n At Time: ' + str(timenow2))
                f.close()

                print("ok 4")
        print("Auto End")
        add_file('wallet.txt','\n----------------------------------------------------------------------------------------------------------')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import csv
import secrets
from eth_account import Account
from datetime import datetime
from datetime import date
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


# Var
delay = 20
ref = 'https://blursea.io/'
# webrd = 'https://vanity-eth.tk/'
ii = 1
h = 0

check0 = '//*[@id="airdrop-form"]/div/input'
check1 = '//*[@id="airdrop-form"]/div/button'
check2 = '#airdrop-block > div.col-12.col-sm-10.col-md-9.col-lg-8 > div.row.mt-4.text-center.justify-content-between > div:nth-child(2) > div.heading-h5.text-primary'
check02 = '#airdrop-block > div.col-12.col-sm-10.col-md-9.col-lg-8 > div.text-break > span.text-primary.copy'
check3 = '//*[@id="airdrop-form"]/div/input'
check4 = '#withdraw'
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
def wait (b,a):
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((b, a)))

# Auto programming

with open('data.csv') as f:
    reader = csv.reader(f,delimiter='|')
    l = [row for row in reader]
    with open("data.csv") as f:
        reader = csv.reader(f)
        for i in reader:
            swap = l[h][1]
            swap2 = l[h][0]
            while True:
                try:
                    print(swap)
                    print(swap2)
                    print("Dang Auto Cho Wallet: ",swap)
                    h += 1
                    driver = webdriver.Chrome(executable_path="C:/Users/lehuy/Documents/cd/chromedriver.exe")
                    driver.get(ref)
                    wait(By.XPATH,check1)
                    cs1 = driver.find_element(By.XPATH,check0)
                    time.sleep(1)
                    cs1.send_keys(swap)
                    time.sleep(1)
                    ip2 = driver.find_element(By.XPATH, check1)
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", ip2)
                    wait(By.CSS_SELECTOR,check02)
                    ii1 = driver.find_element(By.CSS_SELECTOR,check2)
                    print(ii1.text)
                    time.sleep(1)
                    iiok = 50 - int((ii1.text))
                    print(iiok)
                    ii11 = ii1.text
                    time.sleep(1)
                    refok = driver.find_element(By.CSS_SELECTOR,check02)
                    print('check02',refok.text)
                    print('check iiok',iiok)
                    write = open('data1.txt','w')
                    write.write(refok.text)
                    write.close()

                    driver.close()

                    read = open('data1.txt','r')
                    refokok = read.read()
                        
                    
                    for ii in range(iiok):
                        key = "0x" + secrets.token_hex(32)
                        address = Account.from_key(key).address
                        print('Address: ' + str(address) + '|' + str(key))
                        add_file('wallet.txt',key+'|'+address)
                        address2 = address
                        while True:
                            try:
                                driver = webdriver.Chrome(executable_path="C:/Users/lehuy/Documents/cd/chromedriver.exe")
                                driver.get(refokok)
                                wait(By.XPATH,check1) 
                                ip = driver.find_element(By.XPATH, check3)
                                ip.send_keys(address2)
                                # time.sleep(2)
                                ip3 = driver.find_element(By.XPATH, check1)
                                time.sleep(1)
                                driver.execute_script("arguments[0].click();", ip3)
                                time.sleep(5)
                                
                            except:
                                continue
                            break
                        print("Dang Auto Lan Thu " + str(ii) + " Cho Wallet:" + str(swap))
                        driver.quit()
                        # time.sleep(2)
                        #  Report Result
                    
                        
                    print('ok 3')
                    
                    now2 = datetime.now()
                    timenow2 = now2.strftime("%d/%m/%Y, %H:%M:%S")
                    if iiok == 0:
                        driver = webdriver.Chrome(executable_path="C:/Users/lehuy/Documents/cd/chromedriver.exe")
                        driver.get(ref)
                        wait(By.XPATH,check1)
                        print('ok 4')
                        cs1ok = driver.find_element(By.XPATH,check0)
                        cs1ok.send_keys(swap)
                        time.sleep(1)
                        ip2ok = driver.find_element(By.XPATH, check1)
                        driver.execute_script("arguments[0].click();", ip2ok)
                        wait(By.CSS_SELECTOR,check4)
                        okwdok = driver.find_element(By.CSS_SELECTOR, check4)
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", okwdok)
                        driver.quit()
                        print('Da Click Withdraw!!!')
                        f = open('log.txt',"a")
                        f.write('\n'+str(ii11) +' With ADDRESS : ' + str(swap) + '|' + str(swap2) + '\n At Time: ' + str(timenow2))
                        f.close()
                    else:
                        f = open('log.txt',"a")
                        f.write('\n' + str(ii11)+ ' Fail With ADDRESS : ' + str(swap) + '|' + str(swap2) + '\n At Time: ' + str(timenow2))
                        f.close()
                        print("ok 5")
                except:
                     continue
                break
            print("Auto End")
            add_file('wallet.txt','\n----------------------------------------------------------------------------------------------------------')
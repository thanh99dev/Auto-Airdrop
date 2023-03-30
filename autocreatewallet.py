import secrets
from eth_account import Account
in1 = int(input("So vi ban muon tao: "))


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
for i in range(in1):
    key = "0x" + secrets.token_hex(32)
    address = Account.from_key(key).address

    print('Address: ' + str(address) + '|' + str(key))
    add_file('wallet.txt',key+'|'+address)
add_file('wallet.txt','\n-------------------------------------------------------------------------------------')



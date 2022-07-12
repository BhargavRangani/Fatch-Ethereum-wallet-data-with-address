from requests import get
from matplotlib import pyplot as plt
from datetime import datetime

##### ACCOUNT BALANCE ####
API_KEY = "919UYCP9TGBM4BQM834VQXDP9QJX61D72M"
BASE_URL = "https://api.etherscan.io/api"
ETHER_VALUE = 10 ** 18

def make_api_url(module, action, address, **kwargs):
    url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

    for key, value in kwargs.items():
        url += f"&{key}={value}"

    return url

def get_account_balance(address):
        balance_url = make_api_url("account", "balance", address, tag="latest")
        response = get(balance_url)
        data = response.json()

        #print(int(data["result"]) / ETHER_VALUE)
        value = int(data["result"]) / ETHER_VALUE
        return value

#address = "0xddfAbCdc4D8FfC6d5beaf154f18B778f892A0740"
#eth = get_account_balance(address)
#print("Your Ethereum wallet balance: ",eth)

#### ACCOUNT TRANSACTIONS ####

def get_transactions(address):
    transactions_url = make_api_url("account", "txlist", address, startblock=0, endblock=99999999, page=1, offset=count, sort="asc")
    response = get(transactions_url)
    data = response.json()["result"]

    for tx in data:
            trans_hash = tx["hash"]
            to_addr = tx["to"]
            from_addr = tx["from"]
            value = int(tx["value"]) / ETHER_VALUE
            status = tx["txreceipt_status"]
            gas = int(tx["gasUsed"])* int(tx["gasPrice"]) / ETHER_VALUE
            time = datetime.fromtimestamp(int(tx["timeStamp"]))
            print("--------------------------------------------------------------------------------------")
            print("Transaction hash: ",trans_hash)
            print("To: ", to_addr)
            print("From: ", from_addr)
            print("Status: ", status)
            print("Value: ", value)
            print("Time: ", time)
            print("Gas Used: ", gas)   



#address = "0xddfAbCdc4D8FfC6d5beaf154f18B778f892A0740"
print("==================================Transactions========================================")
address = input("Enter eth address: ")
count = input("How many transactions you want to see: ")
get_transactions(address)
print("\n======================================END============================================")
#print("Your Ethereum wallet balance: ",eth)

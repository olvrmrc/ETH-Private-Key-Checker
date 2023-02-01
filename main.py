import os
from eth_account import Account
from web3 import Web3

ether_rpc_url = "https://eth.llamarpc.com"
web3 = Web3(Web3.HTTPProvider(ether_rpc_url))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_key():
    clear()

    key = input('Enter the private key here >>> ')

    account = Account.from_key(key)
    wallet = account.address
    balance = web3.fromWei(web3.eth.getBalance(wallet), 'ether')

    clear()

    input(f'Wallet: {wallet} \nBalance: {balance} ETH')

check_key()
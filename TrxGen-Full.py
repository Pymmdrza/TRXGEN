import random
import colorama
from colorama import Fore,Back,Style

import ecdsa
import base58
import requests
from Crypto.Hash import keccak

def keccak256(data):
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()


def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)


def verifying_key_to_addr(key):
    pub_key: object = key.to_string()
    primitive_adder = b"\x41" + keccak256(pub_key)[-20:]
    Addr: bytes = base58.b58encode_check(primitive_adder)
    return Addr

count = 0
print(Fore.CYAN+"Please Wait..."+Style.RESET_ALL)
while True:
    raw = bytes(random.sample(range(0,256), 32))
    key = get_signing_key(raw)
    Wallet = verifying_key_to_addr(key.get_verifying_key()).decode()
    HexAdd = base58.b58encode_check(Wallet.encode()).hex()
    publickey = key.get_verifying_key().to_string().hex()
    privatekey = raw.hex()
    block = requests.get("https://apilist.tronscan.org/api/account?address="+Wallet)
    res = block.json()
    balances = dict(res)["balance"]
    txid = dict(res)["totalTransactionCount"]
    frozen = dict(res)["totalFrozen"]
    count += 1
    print("TRON Information Account Finder : "+str(count))
    print(Fore.YELLOW+"Address = "+Wallet+" "+Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX+"Private Key = "+privatekey+" "+Style.RESET_ALL)
    print(Fore.YELLOW+"Hex Address = "+HexAdd+" "+Style.RESET_ALL)
    print(Fore.WHITE+"Public Address  = "+publickey+" "+Style.RESET_ALL)
    print(Fore.RED+"Balance Check ="+str(balances)+"  | Transactions = "+str(txid)+" | Frozen = "+str(frozen)+" ]"+" "+Style.RESET_ALL)
    print("==========================[ M M D R Z A . C O M ]=============================\n")
    if int(balances) > 0 or int(txid) > 0 or int(frozen) > 0 :
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||||||WinnerTRX|||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||Address Wallet = "+Wallet)
        print("||Private Key = "+privatekey)
        print("||Public Address = "+publickey)
        print("||Hex Address = "+HexAdd)
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||[   M M D R Z A . C O M   ]|||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        f=open(u"Winner.txt","a")
        f.write("\n|||||||||||||||||||||||||||||||||||||||||||||||||||")
        f.write("Wallet Winner Address = "+Wallet)
        f.write("Private Key = "+privatekey)
        f.write("Public Key = "+publickey)
        f.write("Hex Address = "+HexAdd)
        f.write("||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
        continue


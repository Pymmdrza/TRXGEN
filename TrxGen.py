import random

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
print("Please Wait...")
while True:
    raw = bytes(random.sample(range(0,256), 32))
    key = get_signing_key(raw)
    Wallet = verifying_key_to_addr(key.get_verifying_key()).decode()
    HexAdd = base58.b58encode_check(Wallet.encode()).hex()
    publickey = key.get_verifying_key().to_string().hex()
    count += 1
    privatekey = raw.hex()
    block = requests.get("https://apilist.tronscan.org/api/account?address="+Wallet)
    res = block.json()
    balances = dict(res)["balance"]
    transaction = dict(res)["totalTransactionCount"]
    frozen = dict(res)["totalFrozen"]

    print("TRX Information Wallet :"+str(count))
    print("Address = "+Wallet)
    print("Private Key = "+privatekey)
    print("Hex Address = "+HexAdd)
    print("Public Address = "+publickey)
    print(" ["+" Balance : "+str(balances)+" |"+" Total TXID : "+str(transaction)+" |"+" Frozen : "+str(frozen)+" ]")
    print("================M M D R Z A . C O M ====================")
    if int(balances) > 0 or int(transaction) >0 or int(frozen) > 0:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||Winner Wallet :D||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("Address Winner = "+Wallet)
        print("Private Key Winner = "+privatekey)
        print("Hex Address Winner = "+HexAdd)
        print("Public Address Winner = "+publickey)
        print(" ["+" Balance : "+str(balances)+" |"+" Total TXID : "+str(transaction)+" |"+" Frozen : "+str(frozen)+" ]")
        print("================M M D R Z A . C O M ====================")
        f=open(u"Winner.txt","a")
        f.write("\nPrivate Key = "+privatekey)
        f.write("Account Address = "+Wallet)
        f.write("Hex Address = "+HexAdd)
        f.write("Public Key = "+publickey)
        f.write("================M M D R Z A . C O M ====================")
        f.close()
        continue

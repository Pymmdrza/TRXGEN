import random
import colorama
from colorama import Fore, Back, Style
import ecdsa
import base58
import requests
from Crypto.Hash import keccak
import time

def keccak256(data):
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()


def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)


def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_adder = b"\x41" + keccak256(pub_key)[-20:]
    Addr = base58.b58encode_check(primitive_adder)
    return Addr

start=time.time()
def seek():
    count = 0
    while True:
        raw = bytes(random.sample(range(0, 256), 32))
        key = get_signing_key(raw)
        Wallet = verifying_key_to_addr(key.get_verifying_key()).decode()
        HexAdd = base58.b58encode_check(Wallet.encode()).hex()
        publickey = key.get_verifying_key().to_string().hex()
        privatekey = raw.hex()
        block = requests.get("https://apilist.tronscan.org/api/account?address=" +Wallet)
        res = block.json()
        balances = dict(res)["balance"]
        txid = dict(res)["totalTransactionCount"]
        vipers = dict(res)["transactions_out"]
        frozen = dict(res)["totalFrozen"]
        TYPEX = dict(res)["frozenForBandWidth"]
        TYPEX1 = dict(res)["rewardNum"]
        count += 1
        print(
            "Scan Number : "+str(count) + Fore.GREEN + "\nAddress = " + Wallet + Style.RESET_ALL + " " + Fore.CYAN + "\nPrivate Key = " + privatekey + " " + Style.RESET_ALL + " \n " + Fore.LIGHTRED_EX +"TX " + str(
                txid) +" TPE: " + str(TYPEX) + "  BAL: " + str(balances) + " TXO: " + str(vipers) + " FRZ : " + str(frozen)+" TPS : "+str(TYPEX1) + Style.RESET_ALL)


        if int(txid) > 0:
            print("======================================================")
            print("||Address Wallet = " + Wallet)
            print("||Private Key = " + privatekey)
            print("||Public Address = " + publickey)
            print("||Hex Address = " + HexAdd)
            print("=======================================================")
            f = open(u"Winner.txt", "a")
            f.write("\n====================================================")
            f.write("Wallet Winner Address = " + Wallet)
            f.write("Private Key = " + privatekey)
            f.write("Public Key = " + publickey)
            f.write("Hex Address = " + HexAdd)
            f.write("=========================================================\n")
            continue
seek()

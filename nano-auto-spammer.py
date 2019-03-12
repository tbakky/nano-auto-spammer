from nanocurrency import *
from time import sleep
import requests
import sys

def get_account_info():
    if len(sys.argv) < 5:
        print("NOT ENOUGH ARGS")
        exit(0)

    account_1 = sys.argv[1]
    seed_1 = sys.argv[2]
    key_1 = generate_account_private_key(seed_1, 0)
    account_2 = sys.argv[3]
    seed_2 = sys.argv[4]
    key_2 = generate_account_private_key(seed_2, 0)
    wallet = sys.argv[5]
    return account_1, seed_1, key_1, account_2, seed_2, key_2, wallet

def send(wallet, source, destination, amount):
    r = requests.post(
    "http://127.0.0.1:7076",
    json={"action": "send", "wallet": wallet, "source": source,
        "destination": destination, "amount": amount}
    )
    print(r.json())
    return r.json()["block"]

def main():
    #wallet = "2A0FB86D6023E92C6980ECAAEFD812CDDE993D2BE29D2086933D80AF3AB2C84E"
    account_1, seed_1, key_1, account_2, seed_2, key_2, wallet = \
        get_account_info()

    amount = 1000000

    while True:
        send(wallet, account_2, account_1, amount)
        send(wallet, account_1, account_2, amount)

if __name__ == "__main__":
    main()



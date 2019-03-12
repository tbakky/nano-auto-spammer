from nanocurrency import *
import requests
import sys

def get_account_info():
    if len(sys.argv) < 6:
        print("NOT ENOUGH ARGS")
        exit(0)

    account_1 = sys.argv[1]
    seed_1 = sys.argv[2]
    account_2 = sys.argv[3]
    seed_2 = sys.argv[4]
    wallet = sys.argv[5]
    return account_1, seed_1, account_2, seed_2, wallet

def send(wallet, source, destination, amount):
    r = requests.post(
    "http://127.0.0.1:7076",
    json={"action": "send", "wallet": wallet, "source": source,
        "destination": destination, "amount": amount}
    )
    print(r.json())
    return r.json()["block"]

def main():
    account_1, seed_1, account_2, seed_2, wallet = \
        get_account_info()

    amount = 1000000

    while True:
        send(wallet, account_2, account_1, amount)
        send(wallet, account_1, account_2, amount)

if __name__ == "__main__":
    main()



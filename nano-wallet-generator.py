import sys
from nanocurrency import *

seed = generate_seed()
account_id = generate_account_id(seed, 0)


if len(sys.argv) > 1:
    wallet_name = sys.argv[1]
else:
    print("NOT ENOUGH ARGS: Provide a wallet name")
    exit(0)

with open(wallet_name, 'w') as out:
    out.write(seed)
    out.write('\n')
    out.write(account_id)
    out.write('\n')

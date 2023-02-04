from termcolor import cprint
from config import *
from main import *

if __name__ == "__main__":

    cprint(RUN_TEXT, RUN_COLOR)
    cprint(f'\nsubscribe to us : https://t.me/hodlmodeth', RUN_COLOR)

    for privatekey in KEYS_LIST:

        cprint(f'\n=============== start : {privatekey} ===============', 'white')

        AMOUNT_TO_SWAP = round(random.uniform(AMOUNT_FROM, AMOUNT_TO), 6)

        uniswap_swap(privatekey, AMOUNT_TO_SWAP)
        sleeping(SLEEP_FROM, SLEEP_TO)
        delegate(privatekey)
        sleeping(SLEEP_FROM, SLEEP_TO)


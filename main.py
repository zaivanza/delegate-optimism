from web3 import Web3
from termcolor import cprint
import time
from config import *

def uniswap_swap(privatekey, AMOUNT_TO_SWAP):
    try:

        web3 = Web3(Web3.HTTPProvider(RPC))
        account = web3.eth.account.privateKeyToAccount(privatekey)
        address_wallet = account.address
        nonce = web3.eth.get_transaction_count(address_wallet)

        uniswap_contract = web3.eth.contract(address=web3.toChecksumAddress('0x68b3465833fb72a70ecdf485e0e4c7bd8665fc45'), abi=ABI_UNISWAP) 

        from_token = '0x4200000000000000000000000000000000000006'
        to_token = '0x4200000000000000000000000000000000000042'

        value = intToDecimal(AMOUNT_TO_SWAP, 18) 

        data = uniswap_contract.encodeABI(fn_name="exactInputSingle", args=[(from_token, to_token, 500, address_wallet, value, 1455, 0)],)
        deadline = (int(time.time()) + 10000)
        multicall_function = uniswap_contract.get_function_by_selector("0x5ae401dc")

        contract_txn = {
            'chainId': web3.eth.chain_id, 
            'gas': random.randint(300000, 400000),
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(address_wallet),
            'value': value,
            }

        transaction = multicall_function(deadline, [data]).build_transaction(contract_txn)

        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=privatekey)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        cprint(f'\n>>> swap | https://optimistic.etherscan.io/tx/{web3.toHex(tx_token)}', 'green')

    except Exception as error:
        cprint(f'\n>>> swap | {address_wallet} | {error}', 'red')

def delegate(privatekey):
    try:

        web3 = Web3(Web3.HTTPProvider(RPC))
        account = web3.eth.account.privateKeyToAccount(privatekey)
        address_wallet = account.address
        nonce = web3.eth.get_transaction_count(address_wallet)

        contractToken = '0x4200000000000000000000000000000000000042'
        contract = web3.eth.contract(address=contractToken, abi=ABI_DELEGATE)

        contract_txn = contract.functions.delegate(
            address_wallet
        ).build_transaction({
        'from': address_wallet,
        'gas': random.randint(300000, 400000),
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce,
        })
            
        signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key=privatekey)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

        cprint(f'>>> delegate | https://optimistic.etherscan.io/tx/{web3.toHex(tx_token)}', 'green')

    except Exception as error:
        cprint(f'>>> delegate | {address_wallet} | {error}', 'red')

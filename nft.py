import yaml
from web3 import Web3
from eth_account.messages import encode_defunct

import nft_abi

with open('config.yaml') as f:
    config = yaml.safe_load(f)

NFT_CONTRACT_ADDRESS = config['contracts']['nft']  

def verify_nft(web3: Web3, telegram_username: str, signature: str, nft_id: int) -> bool:

    # Código para obtener la dirección del usuario de la base de datos
   
    message = f"Verifying Telegram username: {telegram_username}"
    
    message_hash = encode_defunct(text=message)

    recovered_address = web3.eth.account.recover_message(message_hash, signature=signature)

    # Verificar que la dirección recuperada coincida con la del usuario   

    nft_contract = web3.eth.contract(address=NFT_CONTRACT_ADDRESS, abi=nft_abi.NFT_ABI)

    try: 
        nft_owner = nft_contract.functions.ownerOf(nft_id).call()
    except:
        return False

    return recovered_address.lower() == nft_owner.lower()
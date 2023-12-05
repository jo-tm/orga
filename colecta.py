import yaml
from zksync2.provider import Provider

with open('config.yaml') as f:
    config = yaml.safe_load(f)

DONATION_WALLET = config['wallet']['donations']

class Colecta:

    def __init__(self, provider: Provider, deadline: str):
        self.zksync = ZkSync(provider) 
        self.deadline = parse(deadline)
        self.wallet_address = DONATION_WALLET 

    def get_balance(self) -> int:
        balance = self.zksync.provider.get_balance(self.wallet_address)
        if balance is None:
            return 0
        else:
            return balance.committed.tokens
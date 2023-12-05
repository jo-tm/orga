import yaml

class Config:
    def __init__(self):
        with open("config.yaml") as f:
            config = yaml.safe_load(f)
        
        self.ZKSYNC_PROVIDER = config['nodes']['zksync']
        self.DONATION_WALLET = config['wallet']['donations'] 
        self.GROUP_ID = config['telegram']['group_id']

config = Config()
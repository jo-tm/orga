import yaml

class Blacklist:
    
    def __init__(self, data):
        self.blacklist = data['users'] 

    def is_blacklisted(self, user_id):
        return user_id in self.blacklist
        
if __name__ == '__main__':

    with open('blacklist.yaml') as f:
        data = yaml.safe_load(f)

    blacklist = Blacklist(data)
    
    print(blacklist.is_blacklisted(1234))
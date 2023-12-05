import yaml

class Estatuto:
    def __init__(self, data):
        self.title = data['title']
        self.articles = data['articles']

    def get_article(self, number):
        return self.articles[str(number)]
        
    def num_articles(self):
        return len(self.articles)

if __name__ == '__main__':
    with open('estatuto.yaml') as f:
        data = yaml.safe_load(f)

    estatuto = Estatuto(data)
    
    print(estatuto.get_article(2))
    print(estatuto.num_articles())

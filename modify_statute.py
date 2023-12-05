import yaml
import estatuto

def modify_statute(update: Update, context: CallbackContext) -> None:

    number, text = context.args

    with open('estatuto.yaml') as f:
        data = yaml.safe_load(f)

    statute = estatuto.Estatuto(data)

    # Modificar artículo
    statute.modify_article(number, text)

    # Guardar estatuto actualizado
    with open('estatuto.yaml', 'w') as f: 
        yaml.dump(statute.data, f)

    text = f'Artículo {number} del estatuto modificado'
    update.message.reply_text(text)


class Estatuto:

    def __init__(self, data):
        self.data = data

    def modify_article(self, number, text):
        self.data['articles'][str(number)] = text
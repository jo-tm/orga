# orga - Bot de Telegram para organizaciones

orga es un bot de Telegram para administrar organizaciones, asociaciones civiles y grupos políticos. Permite crear encuestas, elecciones, manejar un estatuto, colectas de fondos y más.

## Funcionalidades

Las principales funcionalidades que incluye actualmente son:

- **Verificación con NFT**: Requiere que los miembros verifiquen la propiedad de un NFT específico para unirse al grupo.
- **Encuestas**: Permite crear encuestas con opción de múltiple respuesta y voto secreto. Las encuestas tienen un periodo de creación y votación.
- **Estatuto**: Maneja el estatuto de la organización como una serie de artículos que pueden crearse y modificarse a través de votación.  
- **Elecciones**: Permite crear elecciones para cargos y órganos de gobierno. Usando los periodos de votación.
- **Colectas**: Permite realizar colectas de fondos con criptomonedas sobre zkSync de forma transparente.
- **Llamadas grupales**: Da la capacidad de agendar llamadas de audio privadas (Telegram) y públicas (Twitter Space).

## Tecnologías

Orgabot utiliza las siguientes tecnologías y librerías de Python:

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Para interactuar con la API de Telegram
- [tweepy](https://www.tweepy.org/) - Para interactuar con la API de Twitter
- [web3.py](https://web3py.readthedocs.io/) - Para verificar la propiedad de NFT sobre Ethereum
- [zksync2](https://zksync2py.readthedocs.io/en/latest/) - Para manejar pagos con zkSync
- [pyyaml](https://pyyaml.org/) - Para leer archivos de configuración 
- sqlite3 - Como base de datos para persistir información

## Instalación

1. Clona este repositorio
2. Crea un entorno virtual Python 
3. Instala las dependencias (`pip install -r requirements.txt`)  
4. Completa la configuración
5. Ejecuta `python bot.py`

## Configuración

La configuración se lee desde archivos YAML:

- `config.yaml`: Configuración general del bot.
- `estatuto.yaml`: Artículos del estatuto.
- `abi.json`: ABI para verificar NFT.

Los parámetros a completar incluyen:

- Tokens de API para Telegram y Twitter
- URLs de los nodos de Ethereum y zkSync 
- Dirección del contrato NFT
- Billeteras para las colectas  

## Licencia

GPL-3.0 license.
# Specificaciones para el Orgabo, Bot de Telegram de Asociaciones Civiles Online

- Que use alguna popular libreria de Bots de Telegram en Python.
- Que se use alguna libreria popular de Twitter en Python.
- Que soporte un Grupo/Canal de Telegram para tenes una Asociacion Civil para Militante Politicos o Sociales.
- En base al contenido de los mensajes de Telegram al bot genera Polls o publica actualizaciones en Telegram con el estado de los Polls.
- Que solamente permita ingresar un nuevo miembro al Canal si la persona demuestra tener un NFT asociado a miembros del Canal.
- Los NFT tienen un numero limitado y se pueden adquiuir en OpenSea.
- El Canal de Telegram tiene un canal de Twitter asociado.
- En canal de Telegram y la Asociacion tienen un Estatuto Interno. Incluir un ejemplo generico de Estatuto Argentino de Asociacion Civil. Incluir en el Estatuto cuestiones de votaciones del Comunicacion y de modificaciones del Estatuto.
- El Canal tiene Polls de diferentes tipos.
- Hay un tipo de Poll que es para publicar un Post en Twitter con alguna manifestaciones politica en forma de Texto. Tambien los Post tiene especificado una imagen de fondo (se definen una lista de imagenes de fono).
- Es importante que durante un periodo de armado del Poll, por ejemplo por defecto 2 horas, los miembros del canal pueden postular alternativas dentro del Poll. Luego de pasado el tiempo de armado del Poll se publica en en grupo el Poll con todas las alternativas (armado:2horas).
- Luego cada Poll de Posts en Twitter tiene un tiempo por defecto de Votacion de 2 horas (votacion:2horas)
- Tambien el proponer un Poll se incluye el Titulo del Poll y el tiempo maximo de armado del Poll (por defecto 2 horas) y el tiempo de votacion. Pueden incluir junto con el mensaje de propuesta del Poll por ejemplo params=armado:1hora;votacion;30min.
- El armado y la votacion de los Poll para Posts de Twitter tienen un tiempo maximo por defecto de 24 horas, no se puede especificar mas que ese tiempo.
- Para publicar publicar en Twitter una comunicacion tienen que haber votado mas del 50% de los miembros del canal. Si no votaron mas del 50% se publica un mensaje avisando que el Poll no alcanzo el Quorum.
- Para recordar que hay que votar en los Polls se publica un recordatorio en el canal cada 30 minutos sobre los Polls pendientes de armado y de votacion.
- Hay tambien un tipo de Poll que se arma y se vota para modificar articulos del Estatuto. Se debe especificar el numero de articulo del Estatuto y el texto que lo reemplaza. Tambien se pueden agregar articulos al Estatuto aunque siempre hay que rechazar los si son contradictorios con articulos existentes.
- Un poll de Modificacion del Estatuto tiene un tiempo de armado de 24 horas en el cual se especifica el numero de articulo a modificar ( o si es un nuevo articulo), y durante este armado se proponen los posible textos que lo reemplazen. En el periodo de votacion, por defecto 24 horas, se vota que texto debe reemplazar al existinte o la primera alternativa del Poll es Sin Cambio (no cambiar ningun articulo si las alternativas son consideradas insuficientes).
- La asociacion tiene Comisión Directiva: encargada de la administración. Lo conforman como mínimo un Presidente, un Secretario y un Tesorero. Esto se elijen cada 3 meses. Son los responsables de administrar el Server del Bot de Telegram, la cuenta de Twitter y actualizar la imagenes que hacen al disenio grafico y logos de la Asociacion. Al igual que la modificacion del Estatuto, los Polls de armado y votacion de cambio de Presidente, Secretario y Tesorero se arman en 24 horas y se votan tambien durante las siguientes 24 horas.
- Tambien hay colectas de dinero via zksync o algun sistema anonimo de transferencia de stablecoins. Estas colectas duran un tiempo maximo de 7 dias (se especifica el tiempo en la creacion). El Tesorero es el responsable de administrar la billetaera de zksync (o similar) y darle el destino prometido a los fondos. Luego de pasados un maximo de 7 dias, pueden ser menos si se especifica, el Tesorero debe publicar un Invoice o Link de Transferencia que acredite en que se gastaron los fondos de la colecta. Si no publica informacion el Bot de Telegram debe publicar un recordatorio en el canal.
- Tambien hay Poll por SI o po NO para expulsar algun miembro por Spam o falta graves morales o eticas. El NFT del expulsado no se destruye pero se agrega a una lista negra que no puede acceder al Canal de Telegram.
- Tambien un tipo de Poll que para hacer llamadas de Audio Grupales Privados a un horario especificado dentro del grupo Telegram. El Presidente, el Secretario y el Tesorero tambien son Admin del Grupo de Telegram.
Tambien hay un tipo de Poll para armar un Spaces en Twitter (tipo de lamada de Audio grupal Publica).


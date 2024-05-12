from pyrogram import Client, filters

B2B = Client(
    "2B",
    api_id = 26671063,
    api_hash = '6b0de6d5d6e342955efeab7da779325d',
    bot_token = "5729532009:AAEKmfLu3Rw80uynjhGpwC7jPvajGu00jFY",
)

# Define una función para responder a mensajes
@B2B.on_message(filters.private)
def echo(bot, message):
    message.reply_text("Hola, soy un bot básico de prueba.")

# Inicia el bot
B2B.run()

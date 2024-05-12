import telebot
import time
import json , asyncio

import nest_asyncio
nest_asyncio.apply()

# Reemplaza esto con tu token de bot de Telegram
TOKEN = '6662831579:AAGE6kesXfZhwII7RcH9asG83aCR5wgJXFc'

# Inicializa el bot
bot = telebot.TeleBot(TOKEN)

# Utiliza un diccionario para almacenar las conversaciones
conversations = {}

# Define una función para manejar los mensajes entrantes
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Si la conversación no existe, crea una nueva
    bin_text = message.text
    code = bin_text.split(" ")[0]
    reg = False

    if code == ".id":
      if message.reply_to_message:
       userid = message.reply_to_message.from_user.id
       chatid = message.reply_to_message.chat.id
       bot.reply_to(message, f"user id: {userid}\nchat id: {chatid}")
      else:  
       userid = message.from_user.id
       chatid = message.chat.id
       bot.reply_to(message, f"user id: {userid}\nchat id: {chatid}")
      print(f'id >> {message.from_user.id} @>> {message.from_user.username} name>> {message.from_user.first_name}')

    if code  == ".ban":
      user_id = None
      if message.reply_to_message:
           user_id = message.reply_to_message.from_user.id
      else:
           user_id = message.text.split(" ")[1]
      if user_id != "4546576":
         try:
            if user_id:
              bot.ban_chat_member(message.chat.id, user_id)
              bot.send_message(message.chat.id, text=f"User with ID {user_id} has been banned.")
            else:
                    bot.send_message(message.chat.id, text="Please reply to a message or specify the user ID to ban.")
         except Exception as e:
                    bot.send_message(message.chat.id, text=f"An error occurred while trying to ban the user: {e}")
      else:
         bot.send_message(message.chat.id, text="You cannot ban the bot.")
      print(f'id >> {message.from_user.id} @>> {message.from_user.username} name>> {message.from_user.first_name}')

    if code  == ".unban":
      user_id = None
      if message.reply_to_message:
           user_id = message.reply_to_message.from_user.id
      else:
           user_id = message.text.split(" ")[1]
      if user_id != "4546576":
         try:
            if user_id:
              bot.unban_chat_member(message.chat.id, user_id)
              bot.send_message(message.chat.id, text=f"User with ID {user_id} has been unbanned.")
            else:
                    bot.send_message(message.chat.id, text="Please reply to a message or specify the user ID to unban.")
         except Exception as e:
                    bot.send_message(message.chat.id, text=f"An error occurred while trying to ban the user: {e}")
      else:
         bot.send_message(message.chat.id, text="You cannot unban the bot.")
      print(f'id >> {message.from_user.id} @>> {message.from_user.username} name>> {message.from_user.first_name}')

    if code == ".ali":
       bot.reply_to(message,"CSC_7200001  Por razones de seguridad, se requiere verificación de la tarjeta.Intenta con otra CC.\n\nCSC_7200006  La moneda seleccionada para este pago no es compatible.Intenta con otra CC  o cambia la moneda de pago a USD.\n\nCSC_7200009  Excede el límite de su tarjeta de crédito o cuenta bancaria debito.Intenta con otra CC o espera 24 horas.\n\nCSC_7200011  Fondos insuficientes en tarjeta o cuenta de pago.Intenta con otra CC.\n\nCSC_7200012  La fecha de caducidad de la tarjeta es incorrecta o la tarjeta ha caducado.Intenta con otra CC.\n\nCSC_7200015  Rechazado por un banco o institución financiera. CC bloqueada.Intenta con otra CC.\n\nCSC_7200017  Compras desde Brasil cuando el CPF es inválido. Revisa el CPF, que sea valido.\n\nCSC_7200020  Algo está mal con la información de la tarjeta.Revisa la informacion o intenta con otra CC.\n\nCSC_7200021  Se introdujo un código CVV incorrecto o CC sin uso.Revisa la informacion de la CC e inetenta de nuevo o intenta con otra CC.\n\nCSC_7200022  La tarjeta no es compatible/Información incorrecta de la tarjeta.Revisa la informacion o intenta con otra CC.  Cambia la moneda de pago a USD.\n\nCSC_7200026 Por razones de seguridad, se requiere verificación de la tarjeta.  Esto pasa cuando estamos usando EXTRA muy usada ya al notar varias cuentas con la misma EXTRA se levanta este parámetro de seguridad.Intenta con otra EXTRA, si no funciona crea nueva cuenta.\n\nCSC_7200034  Información incompleta del pedido, datos de la tarjeta o dirección de envío.Comprobar datos de envío y pago, que estén correctos.\n\nCSC_7200040  Esta tarjeta está restringida por el banco.Intenta con otra CC.\n\nCSC_7200051 La moneda o CC no es compatible con Aliexpress. Intenta con otra CC.\n\nCSC_7200052 Transacción no permitida. Bloqueo de CC.Intenta con otra CC o EXTRA. Posible bloqueo si detecta multiples cuentas.\n\nCSC_7200053 Si estás pagando con un cupón de AliExpress, la compra incumple alguna de las condiciones del cupón. Realiza otra vez el pedido o elimina el cupón e intentalo de nuevo\n\nCSC_7200058 Tarjeta en multiples cuentas. Elimina la tarjeta e intenta con otra CC/EXTRA.\n\nCSC_7200064 Tarjeta sin fondos. Intenta con otra CC.")
# Inicia el bot
    if code == ".me":
      bin_text = message.text
      bin_number = bin_text.split(" ")[1] if len(bin_text.split()) > 1 else None
      if bin_number != False:
        bot.reply_to(message, str(extraer_usuario(message.from_user.id)))

bot.infinity_polling()

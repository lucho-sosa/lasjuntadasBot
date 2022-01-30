# -*- coding: utf-8 -*-

from telegram.ext import (Updater, CommandHandler)
from scrt.var import (TKN)


"""
        al agregarte en cualquier chat o grupo sos cargado en una 
        unica variable que es la peopleForMeet.
"""
# TODO: ver como hacer varios hilos 
# TODO: crear argumento para poder especificar día de la peña

# Variables
peopleForTheMeet = []

def start(update, context):
    ''' START '''
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id, "Bienvenido")

def addme(update, context):
   
    contact = update.message.from_user.username
    for person in peopleForTheMeet:
        if contact == person:
            context.bot.send_message(update.message.chat_id, "Ya fuiste agregado") 
            return
    peopleForTheMeet.append(contact)
    context.bot.send_message(update.message.chat_id, "Ahí te agrego, rey")


def rmme(update, context):
    contact = update.message.from_user.username
    for person in peopleForTheMeet:
        if contact == person:
            peopleForTheMeet.remove(contact)
            context.bot.send_message(update.message.chat_id, "Gobernado") 
            return
    # TODO: crear una lista para mostrar quienes estan
    context.bot.send_message(update.message.chat_id, "queres salir y no entraste, por eso te gorrean")


def acc(update, context):
    comentario = str(len(peopleForTheMeet)) + " "
    num = len(peopleForTheMeet)
    if num == 0:
        comentario+= "(JAJAJAJJA)"
    elif num == 1:
        comentario+= "(que triste)"
    elif num == 2:
        comentario+= "(boe)"
    elif num == 3:
        comentario+= "('vos podes' J. Wagner)"
    elif num == 4:
        comentario+= "(por lo menos hay truco)"
    else:
        comentario+= ""
    numOfPeople = "para la peña son: " +  comentario
    context.bot.send_message(update.message.chat_id, numOfPeople)


def listOfPeople(update, context):
    num = len(peopleForTheMeet)
    if num == 0:
        context.bot.send_message(update.message.chat_id, "no va nadie")
        return   
    listOfPeopleDetails = "Los que van a la peña son:\n"
    person = ""
    for person in peopleForTheMeet:
        listOfPeopleDetails += person+"\n"
    context.bot.send_message(update.message.chat_id, listOfPeopleDetails)


def main():
    # TODO: hacer que el token lo busque en un archivo que este en .gitignore
    TOKEN = TKN
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('addme', addme))
    dp.add_handler(CommandHandler('rmme', rmme))
    # TODO: rm -username | para modificar algun usuario - dar aviso que se quito!
    dp.add_handler(CommandHandler('acc', acc))
    dp.add_handler(CommandHandler('listpeople', listOfPeople))

    # Comienza el bot
    updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
    updater.idle()


if __name__ == '__main__':
    main()

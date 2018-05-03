######################################################################
#                              RED BOT                               #
#                              V 1.0.0                               #
######################################################################


import asyncio
import discord
from discord.ext import commands
import requests
import youtube_dl
import random
import re
import logging
import os
import json

from features import *
from settings import *


client = discord.Client()

######################################################################
#                       GENERATION DES LOGS                          #
######################################################################

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

######################################################################
#                        LANCEMENT DU BOT                            #
######################################################################

@client.event
async def on_ready():
    print('Connexion en cours...')
    print('Nom du BOT: ' + str(client.user.name))
    print('Client ID: ' + str(client.user.id))
    print('Invite URL: ' + 'https://discordapp.com/oauth2/authorize?&client_id=' + client.user.id + '&scope=bot&permissions=8')

######################################################################
#                         COMMANDES ADMIN                            #
######################################################################

@client.event
async def on_message(message):
    # Si l'auteur du message n'est pas le bot et que le message commence par le préfixe de la commande ('!' Par défaut), vérifiez si la commande a été exécutée
    if message.author.id != config.BOTID and message.content.startswith(config.COMMANDPREFIX):
        # Supprimer le préfixe et passer en minuscules pour que les commandes ne soient pas sensibles à la casse
        message.content = message.content[1:].lower()

        # Ferme le BOT - utilisable uniquement par le propriétaire du bot spécifié dans la configuration
        if message.content.startswith('shutdown') and message.author.id == config.OWNERID:
            await client.send_message(message.channel, 'Ok brb, killing my self :gun:')
            await client.logout()
            await client.close()

        # Permet au propriétaire de définir l'état du jeu du bot (Propriétaire à definir dans le fichier config)
        elif message.content.startswith('status') and message.author.id == config.OWNERID:
            await client.change_presence(game=discord.Game(name=message.content[7:]))

        # Message d'aide, envoie un MP avec une liste de toutes les commandes et comment les utiliser correctement
        elif message.content.startswith('help') and message.author.id == config.OWNERID:
            await client.send_message(message.channel, "Voilà un MP! ;)")
            await client.send_message(message.author, helpMessage.helpMessage)

        # Envoie un message personnel avec le lien d'invitation du bot
        elif message.content.startswith('invite'):
            await client.send_message(message.channel, 'Voilà un MP! ;)')
            await client.send_message(message.author, 'Invite URL: ' + 'https://discordapp.com/oauth2/authorize?&client_id=' + client.user.id + '&scope=bot&permissions=66579535')

        # Recherche le second mot suivant pythonhelp dans les docs python
        elif message.content.startswith('pythonhelp'):
            messagetext = message.content
            split = messagetext.split(' ')
            if len(split) > 1:
                messagetext = split[1]
                await client.send_message(message.channel, 'https://docs.python.org/3/search.html?q=' + messagetext)

######################################################################
#                     COMMANDES JEUX + JOKE                          #
######################################################################

        # Poste une blague aléatoire de Chuck Norris - ne pas utiliser, elles sont terribles (EN)
        elif message.content.startswith('joke'):
            chuckJoke = requests.get('http://api.icndb.com/jokes/random?')
            if chuckJoke.status_code == 200:
                chuckJoke = chuckJoke.json()['value']['joke']
                await client.send_message(message.channel, chuckJoke)

        # Parle avec la boule 8Ball
        elif message.content.startswith('8ball'):
            await client.send_message(message.channel, rng.getEightBall())

        # Random Pile ou Face
        elif message.content.startswith('coinflip'):
            await client.send_message(message.channel, rng.getCoinFace())

        # Machines à sous au format emoji pour Discord
        elif message.content.startswith('slots'):
            await client.send_message(message.channel, rng.getSlotsScreen())

######################################################################
#                        COMMANDES ANIMAUX                           #
######################################################################

        # GIF random de Chat
        elif message.content.startswith('catgif'):
            await client.send_message(message.channel, cats.getCatGif())

        # Photo random de Chat
        elif message.content.startswith('cat'):
            await client.send_message(message.channel, cats.getCatPicture())

        # Photo random de Chien
        elif message.content.startswith('dog'):
            await client.send_message(message.channel, dogs.getDogPicture())

        # Photo random de Lapin
        elif message.content.startswith('rabbit'):
            await client.send_message(message.channel, rabbits.getRabbitPicture())

        # Photo random d'araignée 
        elif message.content.startswith('spider'):
            await client.send_message(message.channel, spiders.getSpiderPicture())

        # Photo random de Reptile
        elif message.content.startswith('lizard'):
            await client.send_message(message.channel, lizards.getLizardPicture())

        # Photo random de Girafe
        elif message.content.startswith('giraffe'):
            await client.send_message(message.channel, giraffes.getGiraffePicture())

        # Photo random de Serpent
        elif message.content.startswith('snake'):
            await client.send_message(message.channel, snakes.getSnakePicture())

######################################################################
#                          COMMANDES VOCAL                           #
######################################################################

        # Rejoind le salon vocal de l'auteur du message s'il se trouve dans un salon et que le robot n'est pas actuellement connecté à un salon vocal
        elif message.content.startswith('join'):
            if message.author.voice_channel != None and client.is_voice_connected(message.server) != True:
                global currentChannel
                global player
                global voice
                currentChannel = client.get_channel(message.author.voice_channel.id)
                voice = await client.join_voice_channel(currentChannel)

            elif message.author.voice_channel == None:
                await client.send_message(message.channel, ":x: Vous n'êtes pas dans un salon vocal.")

            else:
                await client.send_message(message.channel, ':exclamation: Je suis déjà dans un salon vocal. Utilisez `!leave` pour me faire partir.')

        # Quittera le salon vocale actuelle
        elif message.content.startswith('leave'):
            if client.is_voice_connected(message.server):
                currentChannel = client.voice_client_in(message.server)
                await currentChannel.disconnect()

        # Joue de la musique en utilisant les mots suivants comme paramètres de recherche ou utilise la vidéo liée si un lien est fourni
        elif message.content.startswith('play'):
            if message.author.voice_channel != None:
                if client.is_voice_connected(message.server) == True:
                    try:
                        if player.is_playing() == False:
                            print('not playing')
                            player = await voice.create_ytdl_player(youtubeLink.getYoutubeLink(message.content))
                            player.start()
                            await client.send_message(message.channel, ':musical_note: En cours de lecture: ' + player.title)

                        else:
                            print('is playing')

                    except NameError:
                        print('name error')
                        player = await voice.create_ytdl_player(youtubeLink.getYoutubeLink(message.content))
                        player.start()
                        await client.send_message(message.channel, ':musical_note: En cours de lecture: ' + player.title)

                else:
                    await client.send_message(message.channel, ':exclamation: Je ne suis pas connecté à un salon vocal. Utilisez `!play` pour me faire rejoindre')

            else:
                await client.send_message(message.channel, ":exclamation: Vous n'êtes pas connecté à un salon vocal. Entrez dans un salon vocal et utilisez `!join` pour me faire rejoindre.")

        # Mettra en pause le lecteur audio
        elif message.content.startswith('pause'):
            try:
                player.pause()

            except NameError:
                await client.send_message(message.channel, ':mute: Pas en cours de lecture audio.')

        # Va reprendre le lecteur audio
        elif message.content.startswith('resume'):
            try:
                player.resume()

            except NameError:
                await client.send_message(message.channel, ':mute: Pas en cours de lecture audio.')

        # Va arrêter le lecteur audio
        elif message.content.startswith('stop'):
            try:
                player.stop()

            except NameError:
                await client.send_message(message.channel, ':mute: Pas en cours de lecture audio.')

######################################################################
#                         AUTRES COMMANDES                           #
######################################################################
        
        # Face commande - Poste une emote visage en random a partir du fichier ./features/SmirkMessageList.py
        elif message.content.startswith('face'):
            await client.send_message(message.channel, random.choice(SmirkMessageList.SmirkMessageList))

        # Drink commande - Poste le nom de la personne + la boission en random a partir du fichier ./features/DrinkMessageList.py
        elif message.content.startswith('drink'):
            msg = '{0.author.mention} '.format(message)
            await client.send_message(message.channel, msg + random.choice(DrinkMessageList.DrinkMessageList))

        # MARCO commande - Poste POLO
        elif message.content.startswith('marco'):
            await client.send_message(message.channel, "**POLO**")

        # Vent commande - Poste un vent !
        elif message.content.startswith('vent'):
            await client.send_message(message.channel, ":wind_blowing_face: ")


client.run(config.TOKEN)
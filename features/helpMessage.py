from settings import *

helpMessage = '''
**Vocal / Musique**

`{0}join`
Va rejoindre le salon vocale dans laquelle vous êtes.

`{0}leave`
Va partir du salon vocale dans laquelle vous êtes.

`{0}play [YouTube Url]` *ou* `{0}play [musique ou video à rechercher]`
Commencera à jouer l'audio de la vidéo / chanson fournie.

`{0}pause`
Mettra en pause le flux audio actuel.

`{0}resume`
Va reprendre le flux audio actuel.

`{0}stop`
Arrêter et terminer le flux audio.

~~**=========================================**~~

**Administrateur**

`{0}invite`
Envoie un message personnel avec le lien d'invitation du bot. (Ne fonctionnera que pour le propriétaire du bot.)

`{0}shutdown`
Va faire la déconnexion et l'arrêt du bot. (Ne fonctionnera que pour le propriétaire du bot.)

`{0}status [status here]`
Définira le statut de jeu du bot. Ne fonctionnera que pour le propriétaire du bot. (Ne fonctionnera que pour le propriétaire du bot.)

~~**=========================================**~~

**Mini-Games**

`{0}joke`
Postes une blague aléatoire Chuck Norris.

`{0}8ball`
Pose n'importe quelle question à 8-Ball.

`{0}coinflip`
Va retourner une pièce et afficher le résultat.

`{0}roll [# of dice] D[# of sides] Example: !roll 3 D6`
Va lancer les dés spécifiés et poster le résultat.

`{0}slots`
Va poster un résultat de machine à sous.

~~**=========================================**~~

**Random Commandes**

`{0}cat`
Va poster une image de chat aléatoire ou gif.

`{0}catfact (ACTUELLEMENT HORS DE COMMANDE INDISPONIBLE)`
Va poster un fait de chat au hasard.

`{0}catgif`
Va poster un gif de chat aléatoire.

`{0}dog`
Va poster une image de chien aléatoire.

`{0}rabbit`
Va poster une image de lapin aléatoire.

`{0}face`
Poste un visage random depuis une DB de +270 visages

~~**=========================================**~~

**Jeux**

`{0}hots [hotslogs player ID]` - Example: !hots 3141592
Publiera le MMR du joueur pour le match rapide et la ligue des héros.

`{0}gwent [Nom de la Carte]` - Example: !gwent Geralt
Va poster la description de la carte et l'image de la carte gwent. A une longueur de recherche maximale de 10 caractères.'''.format(config.COMMANDPREFIX)
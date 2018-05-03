import random

from settings import *

# Returns a random magic 8 Ball message
def getEightBall():
	eightBallMessages = ['Essaye plus tard', 'Essaye encore', "Pas d'avis",
				        'C\'est ton destin', 'Le sort en est jeté', 'Une chance sur deux',
				        'Repose ta question', 'D\'après moi oui', 'C\'est certain', 'Oui absolument',
				        'Tu peux compter dessus', 'Sans aucun doute', 'Très probable',
				        'Oui', 'C\'est bien parti', ':smirk:',
				        'C\'est non', 'Peu probable', 'Faut pas rêver',
				        'N\'y compte pas', 'Impossible']

	return random.choice(eightBallMessages)

# Returns random result to a coin flip
def getCoinFace():
	coinFaces = ['😐 Face', '⓵ Pile']

	return random.choice(coinFaces)

# Returns a random slot machine screen, uses discord emoji in the display
def getSlotsScreen():
	slots = ['chocolate_bar', 'bell', 'tangerine', 'apple', 'cherries', 'seven']
	slot1 = slots[random.randint(0, 5)]
	slot2 = slots[random.randint(0, 5)]
	slot3 = slots[random.randint(0, 5)]
	slot4 = slots[random.randint(0, 5)]

	slotOutput = '|\t:{}:\t|\t:{}:\t|\t:{}:\t|\t:{}:\t|\n'.format(slot1, slot2, slot3, slot4)

	if slot1 == slot2 and slot2 == slot3 and slot3 == slot4 and slot4 != 'seven':
		return slotOutput + ':euro: :euro: GÉNIAL :euro: :euro:'

	elif slot1 == 'seven' and slot2 == 'seven' and slot3 == 'seven' and slot4 == 'seven':
		return slotOutput + ':moneybag: :moneybag: JACKPOT :moneybag: :moneybag:'

	elif slot1 == slot2 and slot3 == slot4 or slot1 == slot3 and slot2 == slot4 or slot1 == slot4 and slot2 == slot3:
		return slotOutput + ':euro: JOLI :euro:'

	else:
		return slotOutput
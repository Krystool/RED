import requests

# Returns a link to a random lizard picture
def getLizardPicture():
    lizardPicture = requests.get('https://loremflickr.com/1920/1080/reptiles')
    if lizardPicture.status_code == 200:
        lizardPicture = lizardPicture.url
        return lizardPicture

    else:
        return 'Erreur 404. Le site est Down.'
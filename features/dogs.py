import requests

# Returns a link to a random dog picture
def getDogPicture():
    dogPicture = requests.get('https://loremflickr.com/1920/1080/dog')
    if dogPicture.status_code == 200:
        dogPicture = dogPicture.url
        return dogPicture

    else:
        return 'Erreur 404. Le site est Down.'
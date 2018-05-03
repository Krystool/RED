import requests

# Returns a link to a random snake picture
def getSnakePicture():
    snakePicture = requests.get('https://loremflickr.com/1920/1080/snakes')
    if snakePicture.status_code == 200:
        snakePicture = snakePicture.url
        return snakePicture

    else:
        return 'Erreur 404. Le site est Down.'
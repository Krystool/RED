import requests

# Returns a link to a random rabbit picture
def getRabbitPicture():
    rabbitPicture = requests.get('https://loremflickr.com/1920/1080/rabbit')
    if rabbitPicture.status_code == 200:
        rabbitPicture = rabbitPicture.url
        return rabbitPicture

    else:
        return 'Erreur 404. Le site est Down.'
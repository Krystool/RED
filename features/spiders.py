import requests

# Returns a link to a random spider picture
def getSpiderPicture():
    spiderPicture = requests.get('https://loremflickr.com/1920/1080/spiders')
    if spiderPicture.status_code == 200:
        spiderPicture = spiderPicture.url
        return spiderPicture

    else:
        return 'Erreur 404. Le site est Down.'
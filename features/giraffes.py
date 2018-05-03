import requests

# Returns a link to a random giraffe picture
def getGiraffePicture():
    giraffePicture = requests.get('https://loremflickr.com/1920/1080/giraffe,girafe')
    if giraffePicture.status_code == 200:
        giraffePicture = giraffePicture.url
        return giraffePicture

    else:
        return 'Erreur 404. Le site est Down.'
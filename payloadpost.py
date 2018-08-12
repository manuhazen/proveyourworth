import requests

url = 'http://www.proveyourworth.net/level3/reaper'
payload = {
    'email': 'manuhazen@outlook.com',
    'name': 'Emmanuel Jimenez',
    'image': 'https://github.com/manuhazen/proveyourworth/blob/master/watermarkedproveyourworth.jpg',
    'resume': 'https://www.linkedin.com/nhome/?trk=',
    'code': 'https://github.com/manuhazen/proveyourworth'
}

r = requests.post(url, params=payload)
print(r.text)

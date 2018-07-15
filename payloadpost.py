import requests

r = requests.post('http://www.proveyourworth.net/level3/reaper')
print(r.text)
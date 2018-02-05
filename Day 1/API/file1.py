import requests
import json


data = {'address' : "NIT Jamshedpur, India"}
resp = requests.get(url="https://maps.googleapis.com/maps/api/geocode/json" , params = data)
res = json.loads(resp.content)
print res['results']



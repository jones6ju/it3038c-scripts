import json
import requests

r = requests.get('http://localhost:3000')

data = r.json()

name = data[0]['name']
color = data[0]['color']



print("The name of this widget is %s and the color is %s" % (name, color))

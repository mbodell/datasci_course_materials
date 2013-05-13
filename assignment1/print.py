import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")

resp = json.load(response)

for i in range(10):
  print resp["results"][i]["text"]

import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")

resp = json.load(response)

results = resp["results"]

for i in range(len(results)):
  print results[i]["text"]

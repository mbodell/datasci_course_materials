import urllib
import json


for j in range(9):
  url = "http://search.twitter.com/search.json?q=microsoft&page=" + str(j + 1)
  response = urllib.urlopen(url)
  
  resp = json.load(response)

  results = resp["results"]

  for i in range(len(results)):
    print results[i]["text"]

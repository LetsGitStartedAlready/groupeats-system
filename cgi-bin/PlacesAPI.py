#!/usr/bin/python
import requests
import json
print("Content-Type: text/html\n\n")
findplacerequest = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Pisticci&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=AIzaSyD1gQaUJgwdFqioPQv7qdPQ_4zVH9jJpzA")

textsearchrequest = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=pizza&region=us&location=40.806735,-73.962742&radius=1500&key=AIzaSyD1gQaUJgwdFqioPQv7qdPQ_4zVH9jJpzA")

jsonParse = json.loads(textsearchrequest.text)

#print(jsonParse)
for i in range(11):
    print(jsonParse['results'][i]['formatted_address'])
    print(jsonParse['results'][i]['name'])
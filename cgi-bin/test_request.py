import requests

#response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&key=AIzaSyD1gQaUJgwdFqioPQv7qdPQ_4zVH9jJpzA')

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
params = {
    'location':-33.8670522,
    'radius':500,
    'types':'food',
    'name':'harbour',
    'key':'AIzaSyD1gQaUJgwdFqioPQv7qdPQ_4zVH9jJpzA'
}

response = requests.get(url=url,params=params)

data = response.json()

print(str(data))
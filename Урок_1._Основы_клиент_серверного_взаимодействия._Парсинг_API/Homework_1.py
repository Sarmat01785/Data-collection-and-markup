from config import TOKEN_ID, TOKEN_SECRET
import requests
from pprint import pprint

# Ключ доступа к API Foursquare
client_id = "TOKEN_ID"
client_secret = "TOKEN_SECRET"

url = f"https://api.foursquare.com/v2/venues/search?categoryId=4d4b7105d754a06374d81259&limit=10&client_id={client_id}&client_secret={client_secret}"

response = requests.get(url)
data = response.json()

for venue in data["response"]["venues"]:
    name = venue["name"]
    address = venue["location"]["address"]
    rating = venue["rating"]

    print(f"{name} - {address}, рейтинг: {rating}")

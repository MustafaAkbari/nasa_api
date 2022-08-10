import requests

API_KEY = "bUBWlQOa5vsgdbkpT58OZx9NX50HBumtqpqWzpL6"
NASA_ENDPOINT = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(url=NASA_ENDPOINT)

print(response.json())

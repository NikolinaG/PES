import requests

URL = "http://api.open-notify.org/astros.json"

conn = requests.get(URL)

data = conn.json()
i = 0

while i < len(data["people"]):
    ime = data["people"][i]["name"]
    print("Ime:", ime)
    i += 1
    
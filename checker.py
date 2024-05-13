import csv
import requests

data = list(csv.reader(open("trottermathURls.csv")))

for [title, url] in data:
    response = requests.get(url)
    if response.status_code != 200:
        print(title, url)

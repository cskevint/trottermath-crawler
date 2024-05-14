import csv
import requests

data = list(csv.reader(open("trottermathURls.csv")))

for row in data:
    title = row[0]
    url = row[1]
    response = requests.get(url)
    if response.status_code != 200:
        print(title, url)

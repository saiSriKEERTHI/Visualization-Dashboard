import json
from dashboard.models import DataEntry

def run():
    with open("jsondata.json", "r") as file:
        data = json.load(file)
        for entry in data:
            DataEntry.objects.create(**entry)

print("Data Loaded Successfully!")

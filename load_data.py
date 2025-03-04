import json
import os
import django
from datetime import datetime

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from dashboard.models import DataEntry

# Load JSON data
json_file_path = os.path.join(os.path.dirname(__file__), "jsondata.json")

if not os.path.exists(json_file_path):
    print("❌ ERROR: jsondata.json not found!")
    exit()

with open(json_file_path, encoding="utf-8") as f:
    data = json.load(f)

# Function to safely convert dates
def parse_date(date_str):
    if not date_str:  # If the field is empty or None
        return None
    try:
        return datetime.strptime(date_str, "%B, %d %Y %H:%M:%S")
    except ValueError:  # If the format is incorrect
        return None

# Insert data into the database
for item in data:
    try:
        DataEntry.objects.create(
            end_year=item.get("end_year", ""),
            intensity=item.get("intensity", 0) or 0,  # Ensure it's always an integer
            sector=item.get("sector", ""),
            topic=item.get("topic", ""),
            insight=item.get("insight", ""),
            url=item.get("url", ""),
            region=item.get("region", ""),
            start_year=item.get("start_year", ""),
            impact=item.get("impact", ""),
            added=parse_date(item.get("added")),
            published=parse_date(item.get("published")),
            country=item.get("country", ""),
            relevance=item.get("relevance", 0) or 0,  # Ensure it's always an integer
            pestle=item.get("pestle", ""),
            source=item.get("source", ""),
            title=item.get("title", ""),
            likelihood=item.get("likelihood", 0) or 0,  # Ensure it's always an integer
        )
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
        continue  # Skip this record and continue with the next one

print("✅ Data Imported Successfully!")


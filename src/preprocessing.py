# Text preprocessing functions for cleaning the message & other fields

# src/preprocessing.py

import re
import json
import os

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text

def preprocess_flood_items(flood_items):
    processed = []
    for item in flood_items:
        item['cleaned_message'] = clean_text(item.get('message'))
        item['cleaned_description'] = clean_text(item.get('description'))
        processed.append(item)
    return processed

if __name__ == "__main__":
    from api_client import fetch_flood_data

    raw_data = fetch_flood_data()
    cleaned_data = preprocess_flood_items(raw_data)

    # Ensure 'data' folder exists
    os.makedirs('data', exist_ok=True)

    # Save cleaned data to JSON file
    with open("data/flood_preprocessed.json", "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=4)

    print(f"✅ Saved {len(cleaned_data)} records to data/flood_preprocessed.json")

    # Optional preview
    for entry in cleaned_data:
        print(entry['cleaned_message'][:150] + "...\n")

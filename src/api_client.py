# Functions to call the UK Flood API and fetch data

# src/api_client.py

import requests

API_URL = "https://environment.data.gov.uk/flood-monitoring/id/floods"

def fetch_flood_data():
    """
    Fetch flood data from UK Environment Agency API and extract essential fields.
    Returns:
        List of dicts with essential flood event data.
    """
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()

    essential_items = []
    for item in data.get('items', []):
        flood_area = item.get('floodArea', {})
        essential_items.append({
            "id": item.get('@id'),
            "description": item.get('description'),
            "eaAreaName": item.get('eaAreaName'),
            "county": flood_area.get('county'),
            "riverOrSea": flood_area.get('riverOrSea'),
            "message": item.get('message'),
            "severity": item.get('severity'),
            "severityLevel": item.get('severityLevel'),
            "timeRaised": item.get('timeRaised'),
        })
    return essential_items


if __name__ == "__main__":
    items = fetch_flood_data()
    for flood in items:
        print(flood)

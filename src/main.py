# Main pipeline orchestrator: calls fetch, preprocess, embed, store in order


# main.py

from api_client import fetch_flood_data
from preprocessing import preprocess_flood_items
from vector_store import upload_to_qdrant

def run_pipeline():
    print("Fetching flood data from API...")
    raw_data = fetch_flood_data()

    print("Preprocessing flood data...")
    cleaned_data = preprocess_flood_items(raw_data)

    print("Uploading data to Qdrant...")
    upload_to_qdrant(cleaned_data)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()


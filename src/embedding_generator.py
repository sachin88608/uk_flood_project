# Sentence-Transformers embedding generation code

# src/embedding_generator.py

from sentence_transformers import SentenceTransformer
from preprocessing import preprocess_flood_items
from api_client import fetch_flood_data

def load_model():
    model = SentenceTransformer("all-MiniLM-L6-v2")  # Downloads & caches the model locally
    return model

def generate_embeddings(model, texts):
    return model.encode(texts, show_progress_bar=True)

def prepare_data_for_embedding():
    raw_data = fetch_flood_data()
    cleaned_data = preprocess_flood_items(raw_data)
    
    # Combine cleaned_message + cleaned_description
    texts = [
        f"{item['cleaned_description']} {item['cleaned_message']}"
        for item in cleaned_data
    ]
    return cleaned_data, texts

if __name__ == "__main__":
    model = load_model()
    cleaned_data, texts = prepare_data_for_embedding()
    embeddings = generate_embeddings(model, texts)

    print(f"Generated {len(embeddings)} embeddings with dimension: {len(embeddings[0])}")

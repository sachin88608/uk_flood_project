# Qdrant client code to insert/update/search embeddings

import json
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
client = QdrantClient(host='localhost', port=6333)
collection_name = 'uk_floods'

def upload_to_qdrant(flood_data):
    """
    Upload preprocessed flood data to Qdrant vector DB.
    flood_data: list of dicts, each with cleaned_message and other metadata.
    """

    # Create collection if not exists (recreate_collection is deprecated)
    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )

    points = []
    for i, item in enumerate(flood_data):
        text_to_embed = item.get('cleaned_message') or item.get('message')
        vector = model.encode(text_to_embed).tolist()

        point = PointStruct(
            id=i,  # numeric ID required by Qdrant
            vector=vector,
            payload={
                "id": item.get("id"),
                "description": item.get("cleaned_description") or item.get("description"),
                "message": text_to_embed,
                "severity": item.get("severity"),
                "timeRaised": item.get("timeRaised")
            }
        )
        points.append(point)

    client.upsert(
        collection_name=collection_name,
        points=points
    )

    print(f"✅ Uploaded {len(points)} flood alerts to Qdrant collection '{collection_name}'")

# src/view_qdrant_data.py

from qdrant_client import QdrantClient

client = QdrantClient(host='localhost', port=6333)
collection_name = "uk_floods"

# Fetch first few points
points, _ = client.scroll(
    collection_name=collection_name,
    limit=5,
    with_payload=True
)

for point in points:
    print(f"\n🔹 ID: {point.id}")
    print("📦 Payload:")
    for key, value in point.payload.items():
        print(f"  {key}: {value}")

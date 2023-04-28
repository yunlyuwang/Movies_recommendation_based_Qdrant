import json
import os
import numpy as np

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams

from config import DATA_DIR, COLLECTION_NAME, QDRANT_HOST, QDRANT_PORT

BATCH_SIZE = 256

if __name__ == '__main__':
    qdrant_client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

    vectors_path = os.path.join(DATA_DIR, 'vectors_movies.npy')
    vectors = np.load(vectors_path)
    vector_size = vectors.shape[1]

    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=vector_size, distance="Cosine")
    )

    payload_path = os.path.join(DATA_DIR, 'useful_movies.json')
    with open(payload_path, 'r') as f:
        data_dict = json.load(f)

    payload_01 = []
    for idx, doc in enumerate(data_dict):
        payload_01.append(data_dict)

    qdrant_client.upload_collection(
        collection_name=COLLECTION_NAME,
        vectors=vectors,
        payload=data_dict,
        ids=None,
        batch_size=BATCH_SIZE,
        parallel=2
    )
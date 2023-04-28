from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.http.models.models import Filter

class NeuralSearcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens', device='cpu')
        self.qdrant_client = QdrantClient(host='localhost', port=6333)

    def search(self, text: str, filter_: dict = None):
        vector = self.model.encode(text).tolist()

        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=Filter(**filter_) if filter_ else None, 
            limit=3
        )

        payloads = [hit.payload for hit in search_result]
        return payloads



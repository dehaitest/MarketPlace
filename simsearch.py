import faiss
import pickle
from sentence_transformers import SentenceTransformer


class SimSearch:
    def __init__(self, top_k=6):
        self.model = SentenceTransformer('distiluse-base-multilingual-cased')
        self.k = top_k
        self.embedding_file = 'embeddings.pkl'

    def sentence_embedding(self, results):
        sentences = [x['description'] for x in results]
        sentence_embeddings = self.model.encode(sentences)
        with open(self.embedding_file, "wb") as fout:
            pickle.dump({'ids': [x['id'] for x in results], 'sentences': sentences, 'embeddings': sentence_embeddings}, fout, protocol=pickle.HIGHEST_PROTOCOL)

    def similar_search(self, query):
        with open(self.embedding_file, "rb") as fin:
            stored_data = pickle.load(fin)
            stored_ids = stored_data['ids']
            stored_sentences = stored_data['sentences']
            stored_embeddings = stored_data['embeddings']
        index = faiss.IndexFlatL2(stored_embeddings.shape[1])
        index.add(stored_embeddings)
        xq = self.model.encode([query])
        D, I = index.search(xq, self.k)
        return [stored_ids[i] for i in I[0]]

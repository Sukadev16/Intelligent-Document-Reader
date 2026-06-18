from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def create_vectorstore(chunks):

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index, chunks, embeddings
# model/embeddings.py — FAISS-free version
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

def create_embeddings():
    df = pd.read_csv("data/careers.csv")
    df["text"] = df["job_role"] + ". " + df["description"] + ". Skills: " + df["required_skills"]
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(df["text"].tolist(), convert_to_numpy=True)

    np.save("data/career_embeddings.npy", embeddings)
    df.to_csv("data/career_data_indexed.csv", index=False)
    print("✅ Saved career_embeddings.npy and career_data_indexed.csv")

if __name__ == "__main__":
    create_embeddings()
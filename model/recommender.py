import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CareerRecommender:
    def __init__(self, data):
        self.data = data

        # Combine job role, description, and skills for richer representation
        self.data["combined_text"] = (
            self.data["job_role"].fillna("") + " " +
            self.data["description"].fillna("") + " " +
            self.data["required_skills"].fillna("")
        )

        # Train TF-IDF model on combined text
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.data["combined_text"])

    def recommend(self, query, top_n=5):
        # Transform the user query
        query_vec = self.vectorizer.transform([query])

        # Calculate similarity
        similarity = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        # Get top N results
        top_indices = similarity.argsort()[-top_n:][::-1]

        # Return top job roles
        return self.data.iloc[top_indices][["job_role", "description", "required_skills"]]
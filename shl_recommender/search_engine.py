import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_index(csv_path):
    df = pd.read_csv(csv_path)
    df.fillna('', inplace=True)  # Avoid NaNs
    df['content'] = df.astype(str).agg(' '.join, axis=1)  # Combine all columns
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['content'])
    return tfidf_matrix, df

def search(query, tfidf_matrix, df, top_k=10):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf.fit(df['content'])
    query_vec = tfidf.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = scores.argsort()[-top_k:][::-1]

    results = []
    for idx in top_indices:
        row = df.iloc[idx]
        results.append({
            "Test Name": row.get("Test Name", "N/A"),
            "Test Type": row.get("Test Type", "N/A"),
            "Duration": row.get("Duration", "N/A"),
            "Remote Testing": row.get("Remote Testing", "N/A"),
            "Adaptive/IRT": row.get("Adaptive/IRT", "N/A"),
            "Link": row.get("Link", "#")
        })

    return results

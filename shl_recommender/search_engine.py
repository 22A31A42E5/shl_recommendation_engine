import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_index(csv_path):
    df = pd.read_csv(csv_path)
    df['content'] = df.fillna('').astype(str).agg(' '.join, axis=1)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['content'])
    return tfidf_matrix, df

def search(query, tfidf_matrix, df, top_k=10):
    tfidf = TfidfVectorizer(stop_words='english')
    query_vec = tfidf.fit(df['content']).transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = scores.argsort()[-top_k:][::-1]
    results = df.iloc[top_indices].to_dict(orient='records')
    return results
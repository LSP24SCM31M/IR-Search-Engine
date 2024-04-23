import os
import pickle
import logging
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


index_file_path = os.path.join(os.path.dirname(__file__), '..', 'spiders', 'index.pkl')
with open(index_file_path, 'rb') as f:
    search_index = pickle.load(f)


document_text = [doc['document'] for doc in search_index.values()]
document_names = [doc['document_name'] for doc in search_index.values()]


logger.info("Document Texts:")
for name, text in zip(document_names, document_text):
    logger.info("Document Name: %s, Text: %s", name, text)


text_to_feature_converter = TfidfVectorizer()
document_features = text_to_feature_converter.fit_transform(document_text)


logger.info("TF-IDF Vocabulary:")
for term, index in text_to_feature_converter.vocabulary_.items():
    logger.info("Term: %s, Index: %d", term, index)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_cosine_similarity():
    user_query = request.args.get('query', 'python')
    
    
    if not user_query:
        return jsonify({'error': 'No query provided'})
    
    
    user_query_features = text_to_feature_converter.transform([user_query])
    
    
    similarity_scores = cosine_similarity(user_query_features, document_features).flatten()
    
    
    query_tfidf_scores = user_query_features.toarray()[0]
    
    
    combined_scores = [{'document_name': name,
                        'cosine_similarity': cosine,
                        'tfidf_score': tfidf}
                       for name, cosine, tfidf in zip(document_names, similarity_scores, query_tfidf_scores)]
    
    
    combined_scores.sort(key=lambda x: x['cosine_similarity'], reverse=True)
    
    
    top_k = min(20, len(combined_scores))
    top_k_results = combined_scores[:top_k]
    
    
    logger.info("TF-IDF Scores:")
    for doc in top_k_results:
        logger.info("Document Name: %s, Cosine Similarity: %f, TF-IDF Score: %f", doc['document_name'], doc['cosine_similarity'], doc['tfidf_score'])
    
    return jsonify(top_k_results)


if __name__ == '__main__':
    app.run(debug=True)

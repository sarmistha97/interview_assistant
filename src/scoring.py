from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def concept_coverage(answer, key_concepts):
    """
    Calculate the concept coverage score for a given answer.

    Parameters:
    answer (str): The answer to evaluate.
    key_concepts (set): A set of key concepts that should be covered in the answer.

    Returns:
    float: The concept coverage score, ranging from 0 to 1.
    """
    answer = answer.lower()
    covered = []
    missing  = []

    for concept in key_concepts:
        if concept.lower() in answer :
            covered.append(concept)
        else:
            missing.append(concept)
    
    if len(key_concepts) == 0:
        return 1.0, covered, missing  # If there are no key concepts, consider it fully covered
    coverage_score = len(covered)/len(key_concepts)

    return coverage_score, covered, missing

#OLD baseline using TF-IDF and cosine similarity
def tfidf_similarity(answer, ideal_answer):

    documents = [answer, ideal_answer]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # safety check
    if tfidf_matrix.shape[0] < 2:
        return 0.0

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    print("Answer:", answer)
    print("Ideal:", ideal_answer)

    return similarity[0][0]

#NEW semantic similarity using sentence transformers
def semantic_similarity(answer, ideal_answer):

    emb1 = model.encode(answer, convert_to_tensor=True)
    emb2 = model.encode(ideal_answer, convert_to_tensor=True)

    similarity = util.cos_sim(emb1, emb2)

    return float(similarity)
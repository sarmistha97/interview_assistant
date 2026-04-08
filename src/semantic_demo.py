from sentence_transformers import SentenceTransformer, util
import warnings
warnings.filterwarnings("ignore")


# load model (only once)
model = SentenceTransformer('all-MiniLM-L6-v2')

# question + ideal answer
question = "Explain binary search and its time complexity"

ideal_answer = """
Binary search works on a sorted array by repeatedly dividing the search space in half.
It compares the target with the middle element and eliminates half of the search space each step.
The time complexity is O(log n).
"""

# take user input
user_answer = input("Your answer:\n")

# convert to embeddings
emb1 = model.encode(user_answer, convert_to_tensor=True)
emb2 = model.encode(ideal_answer, convert_to_tensor=True)

# compute similarity
similarity = util.cos_sim(emb1, emb2)

print("\nSemantic Similarity Score:", round(float(similarity), 3))
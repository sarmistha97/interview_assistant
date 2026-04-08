import streamlit as st
from scoring import semantic_similarity, concept_coverage
import json

#load questions
with open("../data/questions.json") as f :
    data = json.load(f)

st.title("hello world")

#select domain and topic
domain = st.selectbox("choose domain", list(data.keys()))
topic = st.selectbox("choose topic", list(data[domain].keys()))

question_data = data[domain][topic]

st.subheader("Question:")
st.write(question_data["question"])

user_answer = st.text_area("your answer")

if st.button("Submit Answer"):
    coverage_score,covered, missing = concept_coverage(user_answer, question_data["key_concepts"])

    similarity_score = semantic_similarity(user_answer, question_data["ideal_answer"])

    final_score = 0.6 * similarity_score + 0.4 * coverage_score

    st.subheader("RESULTS")
    
    st.write("Coverage score:", round(coverage_score, 2))
    st.write("Similarity score:", round(similarity_score, 2))
    st.write("Final score:", round(final_score, 2))
    st.write("Covered concepts:", covered)
    st.write("Missing concepts:", missing)

    #follow-up questions
    follow_ups = question_data.get("follow_ups", {})

    if missing:
        st.subheader("Follow-up questions")

        for concept in missing:
            if concept in follow_ups:
                st.write(f" {follow_ups[concept]}")

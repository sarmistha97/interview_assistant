import random
from question_engine import load_questions
from scoring import concept_coverage, semantic_similarity

def map_difficulty(diff):
    return {1: "easy", 2: "medium", 3: "hard"}.get(diff, "medium")

def run_interview(question_data):

    print("\nStarting interview...\n")

    question = question_data["question"]
    key_concepts = question_data["key_concepts"]
    ideal_answer = question_data["ideal_answer"]

    print("Question:")
    print(question)

    answer = input("\nType your answer:\n") 

#scoring
    coverage_score, covered, missing = concept_coverage(answer, key_concepts)

    similarity_score = semantic_similarity(answer, ideal_answer)

    final_score = 0.6 * similarity_score + 0.4 * coverage_score

#output
    print("\nCoverage score:", round(coverage_score, 2))
    print("Covered concepts:", covered)
    print("Missing concepts:", missing)

    print("Semantic similarity:", round(similarity_score, 2))
    print("Final score:", round(final_score, 2))

    print("\n==============================")
    print("Interview Finished")

    #get follow-up questions
    follow_ups = question_data.get("follow_ups", {})  

    # ask follow-up questions based on missing concepts
    for concept in missing:
        if concept in follow_ups:
            print("\nFollow-up question on:", concept)
            print(follow_ups[concept])
            follow_answer= input("\nYour answer:\n")  # we can score these as well if desired

            # evaluate follow-up answer
            follow_score = semantic_similarity(follow_answer, ideal_answer)
            print("Follow-up semantic similarity:", round(follow_score, 2))

def main():

    data = load_questions()

    domains = list(data.keys())
    print("Available domains:", domains)

    domain = input("Choose domain: ").lower()

    if domain not in data:
        print("Invalid domain")
        return

    topics = list(data[domain].keys())
    print("Available topics:", topics)

    topic = input("Choose topic: ").lower()

    if topic not in data[domain]:
        print("Invalid topic")
        return

    run_interview(data[domain][topic])

if __name__ == "__main__":
    main()
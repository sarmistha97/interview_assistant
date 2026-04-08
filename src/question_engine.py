import json

def load_questions(path = "../data/questions.json"):
    with open(path, "r") as file:
        return json.load(file)

def get_question(data, domain, topic):
    return data[domain][topic]  

def group_questions(domain_data):

    questions_difficulty = {1: [], 2: [], 3: []}

    for topic, data in domain_data.items():
        difficulty = data["difficulty"]
        questions_difficulty[difficulty].append(data)

    return questions_difficulty
    
def get_answer(question, text):

    question = question.lower()

    if "skill" in question:

        start = text.lower().find("technical skills")

        if start != -1:

            return text[start:start+800]

    return "Sorry, I could not find the answer."
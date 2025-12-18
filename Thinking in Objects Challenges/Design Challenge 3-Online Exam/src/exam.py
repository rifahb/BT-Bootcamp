class Exam:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    # 1. Total number of questions
    def total_questions(self):
        return len(self.questions)

    # 2. List all questions by topic
    def questions_by_topic(self, topic_name):
        return [q for q in self.questions if q.topic.name == topic_name]

    # 3. List all questions by topic and category
    def questions_by_topic_and_category(self, topic_name, category_name):
        return [
            q for q in self.questions
            if q.topic.name == topic_name and q.category.name == category_name
        ]

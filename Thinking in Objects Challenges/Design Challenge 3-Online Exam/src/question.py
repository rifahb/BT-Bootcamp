class Question:
    def __init__(self, question_id, text, category, topic):
        self.question_id = question_id
        self.text = text
        self.category = category
        self.topic = topic

    def __str__(self):
        return f"Q{self.question_id}: {self.text}"

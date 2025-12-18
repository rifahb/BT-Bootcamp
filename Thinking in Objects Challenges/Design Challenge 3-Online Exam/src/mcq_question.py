from question import Question

class MCQQuestion(Question):
    def __init__(self, question_id, text, category, topic, options):
        super().__init__(question_id, text, category, topic)
        self.options = options

    def __str__(self):
        return f"MCQ Q{self.question_id}: {self.text} | Options: {self.options}"
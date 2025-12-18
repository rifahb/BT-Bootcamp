from question import Question

class ParagraphQuestion(Question):
    def __init__(self, question_id, text, category, topic, word_limit):
        super().__init__(question_id, text, category, topic)
        self.word_limit = word_limit

    def __str__(self):
        return f"Essay Q{self.question_id}: {self.text} | Word Limit: {self.word_limit}"
from category import Category
from topic import Topic
from mcq_question import MCQQuestion
from paragraph_question import ParagraphQuestion
from exam import Exam

# Create category and topic
cat1 = Category("Programming")
topic1 = Topic("Python")

# Create questions
q1 = MCQQuestion(1, "What is Python?", cat1, topic1, ["Lang", "Snake"])
q2 = ParagraphQuestion(2, "Explain Python OOP", cat1, topic1, 200)

# Create exam
exam = Exam()
exam.add_question(q1)
exam.add_question(q2)

print("Total Questions:", exam.total_questions())
print("\nQuestions by Topic:")
for q in exam.questions_by_topic("Python"):
    print(f"  - {q}")
print("\nQuestions by Topic & Category:")
for q in exam.questions_by_topic_and_category("Python", "Programming"):
    print(f"  - {q}")

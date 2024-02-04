class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question["text"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
        user_answer = input("Your choice (enter the number): ")
        return user_answer

    def run_quiz(self):
        for question in self.questions:
            user_answer = self.display_question(question)
            correct_answer = str(question["answer"])

            if user_answer == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.\n")

        print(f"You scored {self.score} out of {len(self.questions)}.")

if __name__ == "__main__":
    indian_quiz_questions = [
        {
            "text": "Which river is considered the holiest in Hinduism?",
            "options": ["Ganges", "Yamuna", "Brahmaputra", "Indus"],
            "answer": 1,
        },
        {
            "text": "In which state is the famous Taj Mahal located?",
            "options": ["Rajasthan", "Uttar Pradesh", "Maharashtra", "Madhya Pradesh"],
            "answer": 2,
        },
        {
            "text": "Who is known as the 'Father of the Nation' in India?",
            "options": ["Jawaharlal Nehru", "Sardar Patel", "Subhas Chandra Bose", "Mahatma Gandhi"],
            "answer": 4,
        },
    ]

    quiz = Quiz(indian_quiz_questions)
    print("Welcome to the Indian Quiz!")
    quiz.run_quiz()

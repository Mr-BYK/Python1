class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0

    def getQuestions(self):
        return self.questions[self.questionsIndex]

    def displayQuestion(self):
        question = self.getQuestions()
        print(f"Soru {self.questionsIndex + 1}:{question.text}  ")

        for q in question.choices:
            print("-" + q)

        answer = input("Cevap: ")
        self.guess(answer)
        self.loadQuesiton()

    def guess(self, answer):
        question = self.getQuestions()

        if question.checkAnswer(answer):
            self.score += 1
            self.questionsIndex += 1

    def loadQuesiton(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else:
            self.displayQuestion()

    def showScore(Self):
        print("score", self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionsIndex + 1

        if quesitonNumber > totalQuestion:
            print("Quiz Bitti")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100, '*'))


q1 = Question("En iyi programlama dili hangisidir?", ["py", "java", "c#", "c"], "py")
q2 = Question("En iyi yazar kimdir?", ["Sabahattin Ali", "Özlem Yıldız", "Nurettin Hacı", "Torna Yaşar"],
              "Sabahattin Ali")
q3 = Question("En iyi kitap hangisidir?", ["Kürk Mantolu Madonna", "Osmancık", "Gençliğim", "Tutamayanlar"],
              "Kürk mantolu Madonna")
questions = [q1, q2, q3]

quiz = Quiz(questions)
quiz.loadQuesiton()

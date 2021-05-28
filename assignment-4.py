# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    # checking answer.(true or false)
    def checkAnswer(self, answer):
        return self.answer == answer
  
# Quiz  
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
  
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+q)
    
        answer = input('Your answer:')
        self.guess(answer)
        self.loadQuestion()
  
    def guess(self, answer):
        question = self.getQuestion()
    
        if question.checkAnswer(answer):
            # if the answer is true, user gets 10 points.
            self.score += 10
        self.questionIndex += 1
  
    def loadQuestion(self):
        if len(self.questions)== self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
  
    def showScore(self):
        print("Score:", self.score)
  
    # increasing question number by 1.
    def displayProgress(self):
        total_question = len(self.questions)
        question_number = self.questionIndex + 1
        # made it for avoid errors.
        if question_number > total_question:
            print('Quiz is over.')
        else:
            # title of questions with number.
            print(f'Question {question_number} of {total_question}'.center(100, "*"))

# I would made it with loop but I did not want to.
question_1 = Question('What is the oldest programming language?', ['FORTRAN', 'BASIC', 'Autocode', 'Assembly', 'LISP'],'Assembly')
question_2 = Question('What is the most popular programming language?', ['Python', 'Go','C#', 'Java', 'Javascript'],'Python')
question_3 = Question('Which one is scientific computing package in Python?', ['Numpy', 'Random', 'Turtle','BeautifulSoup','Matplotlib'],'Numpy')
question_4 = Question('Which one is data analysis and manipulation tool in Python?', ['Gorillas', 'Giraffes', 'Pandas','Lions','Donkeys'],'Pandas')
question_5 = Question('Which one is game package in Python?', ['Numpy', 'Pandas', 'Matplotlib','Pygame','Sympy'],'Pygame')
question_6 = Question('How can we find dimensions of numpy arrays ?', ['ndarray.shape', 'ndarray.size', 'ndarray.bize','ndarray.plot','ndarray.t'],'ndarray.shape')
question_7 = Question('Where is the capital of Turkey?', ['Ankara', 'Istanbul', 'Mekka','Jerusalem','Raqqa'],'Ankara')
question_8 = Question('What country is Sicily in?', ['Spain', 'France', 'New Zealand','Madagascar','Italy'],'Italy')
question_9 = Question('Which one is the oldest coin?', ['Bitcoin', 'Ethereum', 'Avalanche','Polkadot','Doge'],'Bitcoin')
question_10 = Question('Who is the CEO of SpaceX?', ['Steve Jobs', 'Jeff Bezos', 'Angela Merkel','Baran Munar','Melon Musk'],'Melon Musk')

# checking result...
def result():
    if quiz.score >= 50:
        print("Congratulations! You made it!!")
    else:
        print("Sorry.You did not succeed it")


questions = [question_1, question_2, question_3, question_4, question_5,\
            question_6,question_7,question_8,question_9,question_10,]

quiz = Quiz(questions)
quiz.loadQuestion()
result()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, 
                             QVBoxLayout, QGroupBox, QRadioButton, 
                             QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    ''' contains the question, one correct answer and three incorrect answers'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list= []
questions_list.append(Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
questions_list.append(Question('A traditional residence of the Yakut people', 'Urasa', 'Yurt', 'Igloo', 'Hut'))
questions_list.append(Question('The state language of Brazil', 'Portuguese', 'English', 'Spanish', 'Brazilian'))
questions_list.append(Question('Select the most appropriate English name for the programming concept to store some data', 'variable', 'variation', 'variant', 'changing'))

app = QApplication([])
 
window = QWidget()
window.setWindowTitle('Memory Card')
 
'''Interface for the Memory Card Application'''
button = QPushButton('Answer') # answer button
question_label = QLabel('The most difficult question in the world!') # question text
 
RadioGroupBox = QGroupBox("Answer options") # group on the screen for radio buttons with answers
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Smurfs')
rbtn_3 = QRadioButton('Chulyms')
rbtn_4 = QRadioButton('Aleuts')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # the vertical ones will be inside the horizontal ones
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answers in the second column
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
 
layout_ans1.addLayout(layout_ans3) # columns are in the same line
 
RadioGroupBox.setLayout(layout_ans1) # “panel” with answer options is ready 

AnsGroupBox = QGroupBox("Test result")
result = QLabel("True/False")
correct_ans = QLabel("Correct answer")
layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(correct_ans)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test results
layout_line3 = QHBoxLayout() # “Answer” button
 
layout_line1.addWidget(question_label, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
 
layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2) # the button should be large
layout_line3.addStretch(1)
 
# Now let’s put the lines we’ve created one under one another:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between the content

def show_result():
    #show answer panel
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText("Next question")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText("Answer")
    RadioGroup.setExclusive(False)    
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if button.text() == "Answer":
        show_result()
    else:
        show_question()

answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_label.setText(q.question)
    correct_ans.setText(q.right_answer)
    show_question()

def show_correct(text):
    result.setText(text)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Correct")
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct("Incorrect")

window.cur_question = -1

def next_question():
    window.cur_question += 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    ask(questions_list[window.cur_question])

def click_ok():
    if button.text() == 'Answer':
        check_answer()
    else:
        next_question()

window.setLayout(layout_card)
next_question()
button.clicked.connect(click_ok)
window.show()
app.exec_()

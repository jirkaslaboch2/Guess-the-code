from PyQt5 import QtWidgets
from PyQt5 import QtGui
import random


code = str(random.randint(0000,9999))
guess = ""

print(code)

app = QtWidgets.QApplication([])

def write(x):
    global guess
    global code
    guess = guess
    guess += x
    textbox.setText(guess)

def check(e):
    global guess
    global code
    if guess == code:
        guess = ""
        textbox.setText(guess)
        winwin.show()
    elif guess != code:
        guess = ""
        textbox.setText(guess)
        losewin.show()

def delete(d):
    global guess
    if d == "d":
        guess = ""
        textbox.setText(guess)



main = QtWidgets.QWidget()
main.setWindowTitle("Guess the code game")

main.resize(500,500)

winwin = QtWidgets.QWidget()
winwin.setWindowTitle("You won!")

losewin = QtWidgets.QWidget()
losewin.setWindowTitle("Access denied!")

layout = QtWidgets.QVBoxLayout()
keypad_layout = QtWidgets.QGridLayout()
winlayout = QtWidgets.QVBoxLayout()
loselayout= QtWidgets.QVBoxLayout()



wintext = QtWidgets.QLabel("Congratulations! You guessed the code correctly!")
winlayout.addWidget(wintext)

losetext = QtWidgets.QLabel("Access denied! The code was incorrect.")
loselayout.addWidget(losetext)

winwin.setLayout(winlayout)
main.setLayout(layout)
layout.addLayout(keypad_layout)
losewin.setLayout(loselayout)

info = QtWidgets.QLabel("Guess the 4 digit code")
layout.addWidget(info)

but0 = QtWidgets.QPushButton("0")
but1 = QtWidgets.QPushButton("1")
but2 = QtWidgets.QPushButton("2")
but3 = QtWidgets.QPushButton("3")
but4 = QtWidgets.QPushButton("4")
but5 = QtWidgets.QPushButton("5")
but6 = QtWidgets.QPushButton("6")
but7 = QtWidgets.QPushButton("7")
but8 = QtWidgets.QPushButton("8")
but9 = QtWidgets.QPushButton("9")
butenter = QtWidgets.QPushButton("Enter")
butdel = QtWidgets.QPushButton("Delete")



but0.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
but1.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
but2.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
but3.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
but4.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
but5.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
but6.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
but7.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
but8.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
but9.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
butenter.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
butdel.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)


keypad_layout.addWidget(but0, 3, 1, 1, 1)
keypad_layout.addWidget(but1, 2, 0, 1, 1)
keypad_layout.addWidget(but2, 2, 1, 1, 1)
keypad_layout.addWidget(but3, 2, 2, 1, 1)
keypad_layout.addWidget(but4, 1, 0, 1, 1)
keypad_layout.addWidget(but5, 1, 1, 1, 1)
keypad_layout.addWidget(but6, 1, 2, 1, 1)
keypad_layout.addWidget(but7, 0, 0, 1, 1)
keypad_layout.addWidget(but8, 0, 1, 1, 1)
keypad_layout.addWidget(but9, 0, 2, 1, 1)
keypad_layout.addWidget(butenter, 3, 2, 1, 1)
keypad_layout.addWidget(butdel, 3, 0, 1, 1)



textbox = QtWidgets.QLineEdit()
layout.addWidget(textbox)

textbox.setReadOnly(True)

main.setStyleSheet("""
    QPushButton {
        font-size: 25px;
        font-weight: bold;
        background-color: #00ff00;
    }
    QLineEdit {
        font-size: 40px;
        background-color: #DA70D6;
    }
    QLabel {
        font-size: 25px;
    }

""")

winwin.setStyleSheet("""
    QWidget {
        font-size: 36px;
        font-weight: bold;
        background-color: #00ff00;
    }
""")

losewin.setStyleSheet("""
    QWidget {
        font-size: 36px;
        font-weight: bold;
        background-color: #FF0000;
    }
""")

but0.clicked.connect(lambda: write("0"))
but1.clicked.connect(lambda: write("1"))
but2.clicked.connect(lambda: write("2"))
but3.clicked.connect(lambda: write("3"))
but4.clicked.connect(lambda: write("4"))
but5.clicked.connect(lambda: write("5"))
but6.clicked.connect(lambda: write("6"))
but7.clicked.connect(lambda: write("7"))
but8.clicked.connect(lambda: write("8"))
but9.clicked.connect(lambda: write("9"))
butenter.clicked.connect(lambda: check("e"))
butdel.clicked.connect(lambda: delete("d"))

shortdel = QtWidgets.QShortcut(QtGui.QKeySequence("backspace"), main)


shortdel.activated.connect(butdel.animateClick)



main.show()
app.exec()
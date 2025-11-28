from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6 import QtCore

def frame3():
    from frames.utils import grid, widgets, clear_widgets
    from frames.frames12 import frame1
    from frames.scorehelperfunctions import progress
    clear_widgets()

    message = QLabel("Your score is:")
    message.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    message.setStyleSheet("font-family:'Shanti';font-size:25px;color:white;margin:100px 0px;")
    widgets["message"].append(message)

    score = QLabel(str(progress["score"]))
    score.setStyleSheet("font-size:100px;color:#8FC740;margin:0 75px;")
    widgets["score"].append(score)

    message2 = QLabel("Congratulations! You passed all the challenges!")
    message2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    message2.setStyleSheet("font-family:'Shanti';font-size:30px;color:white;margin-bottom:75px;")
    widgets["message2"].append(message2)

    button = QPushButton("PLAY AGAIN!")
    button.setStyleSheet("*{background:'#BC006C';padding:25px 0;border:1px solid '#BC006C';color:white;font-family:'Arial';font-size:25px;border-radius:40px;margin:10px 300px;} *:hover{background:'#ff1b9e';}")
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.clicked.connect(frame1)
    widgets["button"].append(button)

    pixmap = QPixmap("logo_bottom.png")
    logo = QLabel()
    logo.setPixmap(pixmap)
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet("padding:10px;margin-top:75px;margin-bottom:20px;")
    widgets["logo"].append(logo)

    grid.addWidget(widgets["message"][-1], 2, 0)
    grid.addWidget(widgets["score"][-1], 2, 1)
    grid.addWidget(widgets["message2"][-1], 3, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 4, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 5, 0, 2, 2)

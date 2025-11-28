from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6 import QtCore

def frame4():
    from frames.utils import grid, widgets, clear_widgets, current_topic_score
    from frames.frames12 import frame2
    score_val = int(current_topic_score)

    clear_widgets()

    message = QLabel("Sorry, you have failed!\n Your score is: ")
    message.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    message.setStyleSheet("font-family:'Shanti';font-size:35px;color:white;margin:75px 5px;padding:20px;")
    widgets["message"].append(message)

    score = QLabel(str(score_val))
    score.setStyleSheet("font-size:100px;color:white;margin:0 75px;")
    widgets["score"].append(score)

    # Try again button
    button = QPushButton("TRY AGAIN!")
    button.setStyleSheet("""
        *{
            padding:25px 0;
            background:'#966b47';
            color:white;
            font-family:'Arial';
            font-size:35px;
            border-radius:40px;
            margin:10px 200px;
        }
        *:hover{background:'#966b47';}
    """)
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.clicked.connect(frame2)
    widgets["button"].append(button)

    pixmap = QPixmap("logo_bottom.png")
    logo = QLabel()
    logo.setPixmap(pixmap)
    logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    logo.setStyleSheet("padding:10px;margin-top:75px;")
    widgets["logo"].append(logo)

    grid.addWidget(widgets["message"][-1], 1, 0)
    grid.addWidget(widgets["score"][-1], 1, 1)
    grid.addWidget(widgets["button"][-1], 2, 0, 1, 2)
    grid.addWidget(widgets["logo"][-1], 3, 0, 1, 2)


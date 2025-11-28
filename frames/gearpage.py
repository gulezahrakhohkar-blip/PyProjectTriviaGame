import json
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QCursor
from PyQt6 import QtCore
from clickableGear_v3 import ClickableWidget

ALL_TOPICS = [
    "Fundamentals",
    "Control Structures",
    "Data Structures",
    "Functions & Scope",
    "OOP",
    "Error & Exception Handling",
    "File Handling",
    "Advanced Topics"
]

with open("data/qna.json", "r") as f:
    TOPIC_QUESTIONS = json.load(f)

def open_topic_window(topic_name):
    """Open the ClickableWidget gear interface for the selected topic."""
    from frames.utils import grid, widgets, clear_widgets
    from frames.show_questions import show_question_page
    from frames import utils
    from frames.frames12 import frame2
    current_topic_score = 0

    clear_widgets()

    button = QPushButton("⬅️")
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.clicked.connect(frame2)
    button.setStyleSheet("""
        *{border-radius:70px;font-size:26px;color:white;padding:0px;}
    """)
    widgets["button"].append(button)
    grid.addWidget(button, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)

    questions_for_topic = TOPIC_QUESTIONS[topic_name]

    clickable_widget = ClickableWidget()
    clickable_widget.setTopicName(topic_name)
    clickable_widget.setQuestions(questions_for_topic)
    clickable_widget.clicked.connect(lambda gear_id: show_question_page(gear_id, questions_for_topic[gear_id]))

    utils.current_gear_widget=clickable_widget
    utils.current_topic_score=0

    clickable_widget.gear_states = ["unanswered"] * 10
    for g in clickable_widget.widgets:
        g["state"] = "unanswered"
        g["enabled"] = True
    clickable_widget.update()

    utils.widgets["clickable"].append(clickable_widget)
    utils.grid.addWidget(clickable_widget, 1, 0, 1, 2)

from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QCursor
from PyQt6 import QtCore
from frames.scorehelperfunctions import get_highest, get_average, get_overall_highest, get_overall_percentage

def frame_stats():
    from frames.utils import grid, widgets, clear_widgets
    from frames.frames12 import frame2
    clear_widgets()

    title = QLabel("Statistics")
    title.setStyleSheet("""
        color:white;font-family:'Arial';font-size:28px;font-weight:bold;margin-top:20px;
    """)
    title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    widgets["title"] = [title]
    grid.addWidget(title, 1, 0, 1, 2)

    # Back button
    button = QPushButton("⬅️")
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.clicked.connect(frame2)
    button.setStyleSheet("border-radius:70px;font-size:26px;color:white;")
    widgets["button"].append(button)
    grid.addWidget(button, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)

    topics = [
        "Fundamentals",
        "Control Structures",
        "Data Structures",
        "Functions & Scope",
        "OOP",
        "Error & Exception Handling",
        "File Handling",
        "Advanced Topics"
    ]

    row = 2

    # Overall
    overall_label = QLabel("Overall")
    overall_label.setStyleSheet("font-size:20px;color:orange;margin-left:50px;margin-top:50px;")
    grid.addWidget(overall_label, row, 0)

    overall_score = QLabel(f"Highest Score: {get_overall_highest()}")
    overall_score.setStyleSheet("color:white;font-size:15px;margin-left:60px;")
    overall_percent = QLabel(f"Win Percent: {get_overall_percentage()}%")
    overall_percent.setStyleSheet("color:white;font-size:15px;margin-left:60px;margin-bottom:30px;")

    grid.addWidget(overall_score, row + 1, 0, 1, 1)
    grid.addWidget(overall_percent, row + 2, 0, 1, 1)

    row += 3

    left_topics = topics[:4]
    right_topics = topics[-4:]
    left_row = row
    right_row = row

    for topic in left_topics:
        _add_topic_stats(topic, left_row, col=0)
        left_row += 3

    for topic in right_topics:
        _add_topic_stats(topic, right_row, col=1)
        right_row += 3

    for i in range(20):
        grid.setRowStretch(i, 1)

def _add_topic_stats(topic, base_row, col):
    from frames.utils import grid
    label = QLabel(topic)
    label.setStyleSheet("font-size:15px;color:orange;margin-left:80px")
    grid.addWidget(label, base_row, col)

    high = get_highest(topic)
    avg = get_average(topic)

    high_label = QLabel(f"Highest Score: {high}")
    high_label.setStyleSheet("color:white;font-size:13px;margin-left:100px;")
    avg_label = QLabel(f"Win Percent: {avg}%")
    avg_label.setStyleSheet("color:white;font-size:13px;margin-left:100px;margin-bottom:15px;")

    grid.addWidget(high_label, base_row + 1, col)
    grid.addWidget(avg_label, base_row + 2, col)

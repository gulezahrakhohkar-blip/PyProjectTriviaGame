from PyQt6.QtWidgets import QLabel, QPushButton, QWidget, QHBoxLayout
from PyQt6.QtGui import QPixmap, QCursor
from PyQt6 import QtCore

def frame1():
    from frames.utils import grid, widgets, clear_stretch
    clear_stretch()
    background = QLabel()
    background.setPixmap(QPixmap("logo1.png"))
    background.setScaledContents(True)
    widgets["background"] = [background]
    grid.addWidget(background, 0, 0, 5, 5)

    button = QPushButton("PLAY NOW!")
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.clicked.connect(frame2)
    button.setStyleSheet("""
        *{border-radius:15px;font-size:15px;color:white;padding:15px;background-color:rgba(0,0,0,80);}
        *:hover{background-color:rgba(56,53,55,180);}
    """)
    widgets["button"].append(button)
    grid.addWidget(button, 3, 0, 1, 5, QtCore.Qt.AlignmentFlag.AlignCenter)

def frame2():
    from frames.utils import clear_widgets, grid, widgets
    from frames.scorehelperfunctions import progress, reset_progress
    from frames.gearpage import open_topic_window
    from frames.stats_frame import frame_stats
    clear_widgets()

    #Back button
    button = QPushButton("⬅️")
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    
    button.clicked.connect(frame1)  
    button.setStyleSheet(
         '''
        *{
            border-radius: 70px;
            font-size: 26px;
            color: white;
            padding: 0px 0px;
        }
        '''
    )
    widgets["button"].append(button)

    grid.addWidget(button, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)

    # Title
    title = QLabel("Choose Topic")
    title.setStyleSheet('''
        color: white;
        font-family: "Arial";
        font-size: 28px;
        font-weight: bold;
        margin-top: 40px;
    ''')
    title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
    widgets["title"] = [title]
    grid.addWidget(title, 1, 0, 1, 1)


    score_label = QLabel(f"Score: {progress['score']}")
    score_label.setStyleSheet('''
        color: white;
        font-family: "Arial";
        font-size: 18px;
        font-weight: bold;
        margin-right:20px;
    ''')
    score_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    widgets["score"] = [score_label]
    grid.addWidget(score_label, 2, 1, QtCore.Qt.AlignmentFlag.AlignRight)

    # Topics list
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

    unlocked = progress["unlocked_topics"]

    # Topic buttons
    for i, topic in enumerate(topics):
        button = QPushButton(topic)
        button.setFixedHeight(90)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        if topic in progress["completed_topics"]:
            # ✅ Completed topic
            button.setEnabled(False)
            button.setText("✅ " + topic)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 15px;
                    font-size: 18px;
                    text-align: left;
                    padding-left: 15px;
                }
            """)
        elif i < unlocked:
            # 🟢 Unlocked topic
            button.setStyleSheet("""
                QPushButton {
                    background-color: #4fa3d1;
                    color: white;
                    border-radius: 15px;
                    font-size: 18px;
                    text-align: left;
                    padding-left: 15px;
                }
                QPushButton:hover {
                    background-color: #00C080;
                }
            """)
            button.clicked.connect(lambda _, t=topic: open_topic_window(t))
        else:
            # 🔒 Locked topic
            button.setEnabled(False)
            button.setText("🔒 " + topic)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #2e5a77;
                    color: #aaaaaa;
                    border-radius: 15px;
                    font-size: 18px;
                    text-align: left;
                    padding-left: 15px;
                }
            """)

        grid.addWidget(button, i + 3, 0, 1, 2)

    # === RESET BUTTON ===
    reset_btn = QPushButton("Reset Progress")
    reset_btn.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    reset_btn.setFixedHeight(50)
    reset_btn.setStyleSheet("""
        QPushButton {
            color: white;
            border-radius: 8px;
            font-size: 18px;
            background-color: #c97b37;
        }                  
        QPushButton:hover {
            background-color: #956b48;
        }
    """)
    reset_btn.clicked.connect(reset_progress)

     #Statistics Button
    stats_btn = QPushButton("📊")
    stats_btn.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    stats_btn.setFixedSize(40,40)
    stats_btn.clicked.connect(frame_stats)
    stats_btn.setStyleSheet("""
        QPushButton {
            color: white;
            border-radius: 15px;
            font-size: 40px;
        }

    """)

    grid.setRowStretch(len(topics) + 2, 2)

    bottom_row = QWidget()
    hbox = QHBoxLayout()
    hbox.setContentsMargins(10, 10, 10, 10)
    #hbox.setSpacing(20)
    
    hbox.addWidget(stats_btn)
    hbox.addWidget(reset_btn)

    bottom_row.setLayout(hbox)
    grid.addWidget(stats_btn, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)

    grid.addWidget(bottom_row, len(topics) + 4, 0, 1, 2)
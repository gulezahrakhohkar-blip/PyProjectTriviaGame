from PyQt6.QtWidgets import QLabel, QPushButton, QSizePolicy
from PyQt6.QtGui import QCursor
from PyQt6 import QtCore
from PyQt6.QtCore import QTimer
from frames import utils as lu
from frames.scorehelperfunctions import progress, update_score, save_progress, refresh_score
from frames.gearpage import ALL_TOPICS


def show_question_page(gear_id, question_data):
    from frames.frames12 import frame2

    if lu.current_gear_widget is not None:
        lu.current_gear_widget.setParent(None)

    lu.clear_widgets()

    lu.grid.setColumnStretch(0, 1)
    lu.grid.setColumnStretch(1, 1)

    button = QPushButton("⬅️")
    button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    button.clicked.connect(frame2)
    button.setStyleSheet("border-radius:70px;font-size:26px;color:white;")
    lu.widgets["button"].append(button)
    lu.grid.addWidget(button, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)

    score_label = QLabel(f"Score: {progress['score']}")
    score_label.setStyleSheet("color:white;""font-size:18px;""font-weight:bold;""margin-right:20px;")
    score_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
    lu.widgets["score"] = [score_label]
    lu.grid.addWidget(score_label, 1, 1, 1, 1)

    question = QLabel(question_data["question"])
    question.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet("""
        font-family:'shanti';
        font-size:25px;
        color:white;
        padding:75px;
        margin-top:40px;
    """)
    lu.widgets["question"].append(question)
    lu.grid.addWidget(question, 1, 0, 1, 2)

    # Answers
    for i, answer in enumerate(question_data["answers"]):
        btn = QPushButton(answer)
        btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        btn.setStyleSheet("""
            *{
                min-width:350px;
                max-width:550px;
                border:3px solid '#bc9d00';
                color:white;
                font-family:'shanti';
                font-size:16px;
                border-radius:25px;
                padding:15px 0;
                margin-top:40px;
            }
            *:hover{background:'#bc9d00';}
        """)
        btn.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        btn.clicked.connect(lambda _, a=answer: check_answer(a, question_data, gear_id))
        lu.widgets[f"answer{i}"] = [btn]
        lu.grid.addWidget(btn, 2 + i // 2, i % 2)

def check_answer(selected, question_data, gear_id):
    """Validate answer, update score and gear, then route next view."""
    global current_gear_widget
    from clickableGear_v3 import ClickableWidget
    from frames.frames12 import frame2
    from frames.frame3 import frame3
    from frames.frame4 import frame4
    

    gear_widget = lu.current_gear_widget
    correct = question_data["correct"]

    if selected == correct:
        result_text = "✅ Correct!"
        update_score()
        refresh_score()
        lu.current_topic_score += 1
        gear_widget.disable_gear(gear_id)
    else:
        result_text = "❌ Wrong!"
        gear_widget.mark_gear_state(gear_id, "wrong")

    result_label = QLabel(result_text)
    result_label.setStyleSheet("color: yellow; font-size: 20px;")
    result_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    lu.grid.addWidget(result_label, 6, 0, 1, 2)

    def return_to_gear():
        lu.grid.removeWidget(result_label)
        result_label.deleteLater()

        for key in ["question", "answer0", "answer1", "answer2", "answer3", "score"]:
            if lu.widgets.get(key):
                w = lu.widgets[key].pop()
                lu.grid.removeWidget(w)
                w.deleteLater()

        all_done = all(s in ("correct", "wrong") for s in gear_widget.gear_states)

        if not all_done:
            lu.grid.addWidget(gear_widget, 0, 0, 1, 2)
            gear_widget.update()
            return

        topic_name = gear_widget.topic_name

        if topic_name not in progress["topic_scores"]:
            progress["topic_scores"][topic_name] = []

        progress["topic_scores"][topic_name].append(lu.current_topic_score)

        if lu.current_topic_score > 5:
            progress["completed_topics"].add(topic_name)
            progress["unlocked_topics"] = len(progress["completed_topics"]) + 1
            save_progress()

            if progress["completed_topics"] == set(ALL_TOPICS):
                frame3()
            else:
                frame2()
        else:
            progress["score"] -= lu.current_topic_score
            save_progress()
            frame4()

    QTimer.singleShot(1000, return_to_gear)

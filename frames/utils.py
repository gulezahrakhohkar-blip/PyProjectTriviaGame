from PyQt6.QtWidgets import QGridLayout

# Shared grid layout
grid = QGridLayout()

# Global widget tracker
widgets = {
    "logo": [],
    "button": [],
    "score": [],
    "question": [],
    "answer0": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "message": [],
    "message2": [],
    "clickable": [],
    "score_indicator": [],
    "background": []
}


current_topic_score = 0
current_gear_widget = None

def clear_widgets(exclude_current_gear=False):
    """Remove all widgets from grid and reset dictionary."""
    global current_gear_widget
    while grid.count():
        item = grid.takeAt(0)
        widget = item.widget()
        if widget is not None:
            if exclude_current_gear and widget == current_gear_widget:
                continue
            widget.setParent(None)

    for key in widgets:
        widgets[key] = []

def clear_stretch(exclude_current_gear=False):
    """Reset row/column stretches and clear widgets."""
    clear_widgets(exclude_current_gear)
    for r in range(100):
        grid.setRowStretch(r, 0)
    for c in range(100):
        grid.setColumnStretch(c, 0)

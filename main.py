import sys
from PyQt6.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout
from frames.frames12 import frame1
from frames.utils import grid

app = QApplication(sys.argv)

# Screen setup
screen = app.primaryScreen()
screen_rect = screen.availableGeometry()
w = int(screen_rect.width() * 0.8)
h = int(screen_rect.height() * 1)

window = QWidget()
window.setWindowTitle("Python Trivia Game")
window.resize(w, h)
window.setStyleSheet("background: #397591")

frame1()  # start with splash screen

# Scrollable layout
content_widget = QWidget()
content_widget.setLayout(grid)

scroll = QScrollArea()
scroll.setWidgetResizable(True)
scroll.setWidget(content_widget)

main_layout = QVBoxLayout()
main_layout.addWidget(scroll)
window.setLayout(main_layout)

window.show()
app.exec()

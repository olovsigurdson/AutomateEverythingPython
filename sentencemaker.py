from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox


def make_sentence():
    input1 = int(text.text())
    input2 = int(text2.text())
    value = input1 * input2
    label.setText(str(value))


def current_text():
    text = combo.currentText()
    label.setText(text)


app = QApplication([])
window = QWidget()
window.setWindowTitle("Gör en mening")

layout = QVBoxLayout()

text = QLineEdit()
text2 = QLineEdit()

button = QPushButton(text="Klicka här")

label = QLabel()

combo = QComboBox()
combo.addItem("Svenska")
combo.addItem("Engelsla")

#widget, signal, slot - funktion
button.clicked.connect(make_sentence)
combo.currentTextChanged.connect(current_text)

layout.addWidget(text)
layout.addWidget(text2)
layout.addWidget(combo)
layout.addWidget(button)
layout.addWidget(label)



window.setLayout(layout)
window.show()
app.exec()


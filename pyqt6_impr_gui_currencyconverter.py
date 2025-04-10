from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from BScurrencyconverter import get_currency


def convert_currency():
    input = float(text.text())

    fromcurr = combo.currentText()
    tocurr = combo2.currentText()

    rate = get_currency(fromcurr, tocurr)
    value = input * rate
    label.setText(str(value))


app = QApplication([])
window = QWidget()
window.setWindowTitle("Konvertera valuta")
#Layout
layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()
layout.addLayout(layout1)
layout1.addLayout(layout2)
layout1.addLayout(layout3)

#Två textboxar
text = QLineEdit()

#Knapp
button = QPushButton(text="Konvertera!")

#Label som visar resultatet
label = QLabel()

#Kombobox 1
combo = QComboBox()
combo.addItems(["SEK", "EUR", "USD"])

#Kombobox 2
combo2 = QComboBox()
combo2.addItems(["EUR", "SEK", "USD"])

#widget, signal, slot - funktion
#Knapp och combo
button.clicked.connect(convert_currency)

#Lägger ut layout
layout3.addWidget(text)
layout2.addWidget(combo)
layout2.addWidget(combo2)
layout3.addWidget(button, alignment=Qt.AlignmentFlag.AlignBottom)
layout.addWidget(label)



window.setLayout(layout)
window.show()
app.exec()



#print(get_currency('EUR', 'SEK'))
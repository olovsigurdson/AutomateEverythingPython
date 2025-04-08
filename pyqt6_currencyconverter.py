from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
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
#Layou
layout = QVBoxLayout()

#Två textboxar
text = QLineEdit()

#Knapp
button = QPushButton(text="Konvertera!")

#Label som visar resultatet
label = QLabel()

#Kombobox 1
combo = QComboBox()
combo.addItem("SEK")
combo.addItem("EUR")
combo.addItem("USD")

#Kombobox 2
combo2 = QComboBox()
combo2.addItem("SEK")
combo2.addItem("EUR")
combo2.addItem("USD")

#widget, signal, slot - funktion
#Knapp och combo
button.clicked.connect(convert_currency)

#Lägger ut layout
layout.addWidget(text)
layout.addWidget(combo)
layout.addWidget(combo2)
layout.addWidget(button)
layout.addWidget(label)



window.setLayout(layout)
window.show()
app.exec()



#print(get_currency('EUR', 'SEK'))
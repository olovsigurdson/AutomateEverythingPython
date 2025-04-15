from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt

def get_atomic_number():
    input_atomic = input_text.text().capitalize()

    elements = {
        "H": {"name": "Hydrogen", "atomic_number": 1},
        "He": {"name": "Helium", "atomic_number": 2},
        "Li": {"name": "Lithium", "atomic_number": 3},
        "Be": {"name": "Beryllium", "atomic_number": 4},
        "B": {"name": "Boron", "atomic_number": 5},
        "C": {"name": "Carbon", "atomic_number": 6},
        "N": {"name": "Nitrogen", "atomic_number": 7},
        "O": {"name": "Oxygen", "atomic_number": 8},
        "F": {"name": "Fluorine", "atomic_number": 9},
        "Ne": {"name": "Neon", "atomic_number": 10},
        "Na": {"name": "Sodium", "atomic_number": 11},
        "Mg": {"name": "Magnesium", "atomic_number": 12},
        "Al": {"name": "Aluminum", "atomic_number": 13},
        "Si": {"name": "Silicon", "atomic_number": 14},
        "P": {"name": "Phosphorus", "atomic_number": 15},
        "S": {"name": "Sulfur", "atomic_number": 16},
        "Cl": {"name": "Chlorine", "atomic_number": 17},
        "Ar": {"name": "Argon", "atomic_number": 18},
        "K": {"name": "Potassium", "atomic_number": 19},
        "Ca": {"name": "Calcium", "atomic_number": 20},
        "Sc": {"name": "Scandium", "atomic_number": 21},
        "Ti": {"name": "Titanium", "atomic_number": 22},
        "V": {"name": "Vanadium", "atomic_number": 23},
        "Cr": {"name": "Chromium", "atomic_number": 24},
        "Mn": {"name": "Manganese", "atomic_number": 25},
        "Fe": {"name": "Iron", "atomic_number": 26},
        "Co": {"name": "Cobalt", "atomic_number": 27},
        "Ni": {"name": "Nickel", "atomic_number": 28},
        "Cu": {"name": "Copper", "atomic_number": 29},
        "Zn": {"name": "Zinc", "atomic_number": 30}
    }

    try:
        value = f"{elements[input_atomic]['name']}: Atomic number {elements[input_atomic]['atomic_number']}"
        label_atomic_converted.setText(value)
    except KeyError:
        value = f"{input_atomic} finns ej som grundämne"
        label_atomic_converted.setText(value)


app = QApplication([])
window = QWidget()
window.setWindowTitle("Atomic!")
layout = QVBoxLayout()
label_atomic_converted = QLabel()
input_text = QLineEdit()

label = QLabel('Skriv en bokstav från det periodiska systemet så kommer dess namn ploppa fram!')
open_bt = QPushButton('Check!')

open_bt.clicked.connect(get_atomic_number)

layout.addWidget(label)
layout.addWidget(input_text, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(open_bt, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(label_atomic_converted, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()


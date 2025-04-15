from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from pathlib import Path


def open_file():
    #QFileDialog returnerar två värden. _ är bara en throwaway varaiabel som vi inte behöver
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Välj filer')
    files_opened = []
    for i in filenames:
        path = Path(i)
        files_opened.append(path.stem)
    label_pres_files.setText("These files will be raderade:")
    label_files.setText('\n'.join(files_opened))


def delete_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()


app = QApplication([])
window = QWidget()
window.setWindowTitle("Destroy Erase Improve")
layout = QVBoxLayout()
label_pres_files = QLabel()
label_files = QLabel()

label = QLabel('Välj vilka filer du vill radera. Dessa kommer bli <font color="red"> permanent </font> raderade!')
open_bt = QPushButton('Öppna fil')
del_br = QPushButton('Radera fil')

open_bt.clicked.connect(open_file)
del_br.clicked.connect(delete_files)

layout.addWidget(label)
layout.addWidget(open_bt, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(del_br, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(label_pres_files, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(label_files, alignment=Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()


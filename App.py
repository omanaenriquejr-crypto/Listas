import sys
from PyQt5.QtWidgets import QApplication
from ToDoList import ToDoList

app = QApplication(sys.argv)
Ventana = ToDoList()
Ventana.show()
sys.exit(app.exec())
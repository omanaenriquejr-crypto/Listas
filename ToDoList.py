from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
class ToDoList(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        #carga la vista
        uic.loadUi("ToDoList.ui",self)
        self.btnAgregar.clicked.connect(self.AgregarTarea)
        self.btnActualizar.clicked.connect(self.ActualizarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)

    def AgregarTarea(self):
        tarea = self.edtTarea.text()
        if tarea.strip() == "":
            QMessageBox.information(self, "Error: El campo no puede estar vacío")
            self.edtTarea.setFocus()
            return
        self.lstTareas.addItem(tarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()

    def ActualizarTarea(self):
        indice = self.lstTareas.currentRow()
        tarea = self.edtTarea.text()
        if indice == -1:
            QMessageBox.information(self, "Error: Selecciona una tarea de la lista")
            return
        if tarea.strip() == "":
            QMessageBox.information(self, "Error: El campo no puede estar vacío")
            self.edtTarea.setFocus()
            return
        self.lstTareas.item(indice).setText(tarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()

    def EliminarTarea(self):
        indiceTareaBorrar = self.lstTareas.currentRow()
        if indiceTareaBorrar == -1:
            QMessageBox.information(self, "Error: Selecciona una tarea de la lista")
            return
        self.lstTareas.takeItem(indiceTareaBorrar)

#Listo profesor Este es mi codigo (Omaña Chavarria Enrique) 24/11/2026
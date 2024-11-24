import sys
from PySide6 import QtCore, QtGui, QtWidgets
from app.main.main import WindowMain

app = QtWidgets.QApplication(sys.argv)

window = WindowMain()
window.show()
app.exec()


app.shutdown()
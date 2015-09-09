import sys
from fasade import QtGui, WykresApp

app = QtGui.QApplication(sys.argv)
myapp = WykresApp()  # deklaracja fasady
myapp.show()         # uruchomienie fasady
sys.exit(app.exec_())

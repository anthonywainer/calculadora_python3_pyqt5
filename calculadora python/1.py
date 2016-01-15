import sys
from PyQt5.QtWidgets import QApplication, QDialog


app = QApplication(sys.argv)
window = QDialog()


window.show()
sys.exit(app.exec_())

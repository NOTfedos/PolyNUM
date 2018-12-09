import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from pui import UI_MainWindow
import polys


class PolyWidget(QMainWindow, UI_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_sum.clicked.connect(self.sum_clicked)
        self.btn_sub.clicked.connect(self.sub_clicked)
        self.btn_mult.clicked.connect(self.mult_clicked)
        self.btn_div.clicked.connect(self.div_clicked)
        self.btn_dxdy.clicked.connect(self.dxdy_clicked)
        self.btn_eq.clicked.connect(self.eq_clicked)
        self.to_eq = False

    def sum_clicked(self):
        pol1 = line_polynom.text()
        last_polynom.setText(pol1)
        line_polynom.setText('')
        while not self.to_eq:
            pass
        pol2 = line_polunom.text()
        line_polynom.setText(polys.sum(pol1, pol2))
        self.to_eq = False

    def sub_clicked(self):
        pol1 = line_polynom.text()
        last_polynom.setText(pol1)
        line_polynom.setText('')
        while not self.to_eq:
            pass
        pol2 = line_polunom.text()
        line_polynom.setText(polys.sub(pol1, pol2))
        self.to_eq = False

    def mult_clicked(self):
        pol1 = line_polynom.text()
        last_polynom.setText(pol1)
        line_polynom.setText('')
        while not self.to_eq:
            pass
        pol2 = line_polunom.text()
        line_polynom.setText(polys.mult(pol1, pol2))
        self.to_eq = False

    def div_clicked(self):
        pol1 = line_polynom.text()
        last_polynom.setText(pol1)
        line_polynom.setText('')
        while not self.to_eq:
            pass
        pol2 = line_polunom.text()
        line_polynom.setText(polys.div(pol1, pol2))
        self.to_eq = False

    def dxdy_clicked(self):
        pol1 = line_polynom.text()
        last_polynom.setText(pol1)
        line_polynom.setText(polys.dxdy(pol1))

    def eq_clicked(self):
        self.to_eq = True


app = QApplication(sys.argv)
prw = PolyWidget()
prw.show()
sys.exit(app.exec_())

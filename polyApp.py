import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog
from PyQt5.QtGui import QPixmap
from pui import Ui_MainWindow
import polys
from polys import InvalidMults


IMAGE_PATH = 'polynom_image.png'

class PolyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_sum.clicked.connect(self.sum_clicked)
        self.btn_sub.clicked.connect(self.sub_clicked)
        self.btn_mult.clicked.connect(self.mult_clicked)
        self.btn_div.clicked.connect(self.div_clicked)
        self.btn_dxdy.clicked.connect(self.dxdy_clicked)
        self.btn_eq.clicked.connect(self.eq_clicked)
        self.btn_calculate.clicked.connect(self.pol_calc)
        self.btn_save_pict.clicked.connect(self.save_pict)
        self.cur_proc = self.to_str
        self.arg = ['', '']

    def to_str(self, p_args):
        try:
            self.line_polynom.setText(polys.get_str(p_args[1]))
            polys.get_pict(polys.get_str(self.arg[1]), IMAGE_PATH)
            self.poly_formula.setPixmap(QPixmap(IMAGE_PATH))
        except InvalidMults:
            pass

    def save_pict(self):
        path, okBtnPressed = QInputDialog.getText(self, '',
                                                  'Введите название файла')
        if okBtnPressed:
            s = self.line_polynom.text()
            try:
                polys.get_pict(polys.get_str(s), path)
            except InvalidMults:
                polys.get_pict(s, path)

    def sum_clicked(self):
        self.arg = [self.line_polynom.text(), '']
        self.cur_proc = self.polysum
        self.line_polynom.setText('')
        try:
            self.last_polynom.setText(polys.get_str(self.arg[0]))
            polys.get_pict(polys.get_str(self.arg[0]), IMAGE_PATH)
            self.poly_formula.setPixmap(QPixmap(IMAGE_PATH))
        except InvalidMults:
            pass

    def polysum(self, p_args):
        pol1 = p_args[0]
        pol2 = p_args[1]

        try:
            p = polys.sum_p(pol1, pol2)
            self.line_polynom.setText(p)
            self.last_polynom.setText(p)
            polys.get_pict(p, IMAGE_PATH)
            self.poly_formula.setPixmap(QPixmap(IMAGE_PATH))
        except InvalidMults:
            self.line_polynom.setText('Неверно введен(ы) многочлен(ы)')

    def sub_clicked(self):
        self.arg = [self.line_polynom.text(), '']
        self.cur_proc = self.polysub
        self.line_polynom.setText('')
        try:
            self.last_polynom.setText(polys.get_str(self.arg[0]))
            polys.get_pict(polys.get_str(self.arg[0]), IMAGE_PATH)
            self.poly_formula.setPixmap(QPixmap(IMAGE_PATH))
        except InvalidMults:
            pass

    def polysub(self, p_args):
        pol1 = p_args[0]
        pol2 = p_args[1]

        try:
            p = polys.sub(pol1, pol2)
            self.line_polynom.setText(p)
            self.last_polynom.setText(p)
            polys.get_pict(p, IMAGE_PATH)
            self.poly_formula.setPixmap(QPixmap(IMAGE_PATH))
        except InvalidMults:
            self.line_polynom.setText('Неверно введен(ы) многочлен(ы)')

    def mult_clicked(self):
        self.arg = [self.line_polynom.text(), '']
        self.cur_proc = self.polymult
        self.line_polynom.setText('')
        try:
            self.last_polynom.setText(polys.get_str(self.arg[0]))
            polys.get_pict(polys.get_str(self.arg[0]), IMAGE_PATH)
            self.poly_formula.setPixmap(QPixmap(IMAGE_PATH))
        except InvalidMults:
            pass

    def polymult(self, p_args):
        pol1 = p_args[0]
        pol2 = p_args[1]

        try:
            p = polys.mult(pol1, pol2)
            self.line_polynom.setText(p)
            self.last_polynom.setText(p)
            polys.get_pict(p, IMAGE_PATH)
            self.poly_formula.setPixmap(QPixmap(IMAGE_PATH))
        except InvalidMults:
            self.line_polynom.setText('Неверно введен(ы) многочлен(ы)')

    def div_clicked(self):
        self.arg = [self.line_polynom.text(), '']
        self.cur_proc = self.polydiv

    def dxdy_clicked(self):
        pol1 = self.line_polynom.text()
        self.last_polynom.setText(pol1)
        try:
            self.line_polynom.setText(polys.dxdy(pol1))
        except InvalidMults:
            self.line_polynom.setText('Неверно введен(ы) многочлен(ы)')

    def eq_clicked(self):
        self.arg[1] = self.line_polynom.text()
        try:
            self.last_polynom.setText(polys.get_str(self.arg[1]))
        except InvalidMults:
            pass
        self.cur_proc(self.arg)
        self.cur_proc = self.to_str
        self.arg = ['', '']

    def pol_calc(self):
        try:
            x = float(self.edtXValue.text())
            p = self.line_polynom.text()
            self.edtXResult.setText(str(polys.get_calc(p, x)))
        except ValueError:
            self.edtXResult.setText('Неверное значение аргумента')
        except InvalidMults:
            self.line_polynom.setText('Неверно введен(ы) многочлен(ы)')
            self.edtXResult.setText('')
        self.edtXValue.setText('')


app = QApplication(sys.argv)
prw = PolyWidget()
prw.show()
sys.exit(app.exec_())

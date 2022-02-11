from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from currency_converter import CurrencyConverter
from exchange_design import Ui_MainWindow
from distutils.log import error
import sys

class Excange(QtWidgets.QMainWindow):
    def __init__(self):
        super(Excange, self).__init__()
        self.money = Ui_MainWindow()
        self.money.setupUi(self)
        self.money.pushButton.clicked.connect(self.converter)
    
    def converter(self):
        try:
            exchange = CurrencyConverter()
            my_currency = self.money.enter_currency.text()
            get_currency = self.money.get_currency.text()
            enter_amount = float(self.money.enter_amount.text())
            get_amount = round(exchange.convert(enter_amount, '%s' % (my_currency), '%s' % (get_currency)), 2)
            self.money.get_amount.setText(str(get_amount))
        except:
            error = QMessageBox()
            error.setWindowTitle('Ошибка ввода')
            error.setText('Ввод валюты в заглавных бувах: (USD, EUR)')
            error.setIcon(QMessageBox.Warning)
            # error.setStandardButtons(QMessageBox.Cancel|QMessageBox.OK)
            # error.setDefaultButton(QMessageBox.OK)
            error.setInformativeText('В поле ввода суммы, необходимо ввести цифры: (10.50)')
            error.setDetailedText('Проверте корректность ввода данных')
            error.exec_()
        
        
app = QtWidgets.QApplication([])
application = Excange()
application.show()
 
sys.exit(app.exec())
    
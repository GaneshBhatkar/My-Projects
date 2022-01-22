import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from forex_python.converter import CurrencyRates,CurrencyCodes


class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("Currency_convertor.ui",self)
        self.pushButton.clicked.connect(self.TCP_Settings)
        c = CurrencyRates()
        list1=c.get_rates('USD')
        for x, y in list1.items():
            self.comboBox2.addItem(x)
            self.comboBox1.addItem(x)
        s= CurrencyCodes()
        #self.textBrowser_1.setText(Output_amount)
        self.textBrowser_2.setText(s.get_symbol(self.comboBox1.currentText()))
        self.textBrowser_3.setText(s.get_symbol(self.comboBox2.currentText()))
    

    def TCP_Settings(self):
        Input_Currency      = self.comboBox1.currentText()
        Output_Currency     = self.comboBox2.currentText()
        Input_amount        =self.lineEdit_1.text()
        #Input_Currency      =self.lineEdit_3.text()
        #Output_Currency     =self.lineEdit_4.text()
        c = CurrencyRates()
        Output_Values=c.get_rates(Input_Currency)
        X=format(float(Output_Values[Output_Currency])*float(Input_amount) ,".3f")
        Output_amount=str(X)
        s= CurrencyCodes()
        self.textBrowser_1.setText(Output_amount)
        self.textBrowser_2.setText(s.get_symbol(Input_Currency))
        self.textBrowser_3.setText(s.get_symbol(Output_Currency))
        #self.comboBox1.addItem("Hello World")


app=QApplication(sys.argv)
mainwindow=Login()

widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(320)
widget.setFixedHeight(175)
widget.show()
app.exec_()
import sys
from PyQt5 import QtWidgets, uic
from forex_python.converter import CurrencyRates,CurrencyCodes


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Currency_convertor_window.ui", self)
        self.pushButton.clicked.connect(self.Convertor_Data)
        c = CurrencyRates()
        list1=c.get_rates('USD')
        for x, y in list1.items():
            self.comboBox2.addItem(x)
            self.comboBox1.addItem(x)
        s= CurrencyCodes()
        
        self.textBrowser_2.setText(s.get_symbol(self.comboBox1.currentText()))
        self.textBrowser_3.setText(s.get_symbol(self.comboBox2.currentText()))
    

    def Convertor_Data(self):
        Input_Currency      = self.comboBox1.currentText()
        Output_Currency     = self.comboBox2.currentText()
        Input_amount        =self.lineEdit_1.text()
        
        c = CurrencyRates()
        Output_Values=c.get_rates(Input_Currency)
        X=format(float(Output_Values[Output_Currency])*float(Input_amount) ,".3f")
        Output_amount=str(X)
        s= CurrencyCodes()
        self.textBrowser_1.setText(Output_amount)
        self.textBrowser_2.setText(s.get_symbol(Input_Currency))
        self.textBrowser_3.setText(s.get_symbol(Output_Currency))
       


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
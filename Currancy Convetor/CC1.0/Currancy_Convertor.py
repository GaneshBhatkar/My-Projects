import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from forex_python.converter import CurrencyRates,CurrencyCodes


c = CurrencyRates()
Input_Currency= input("Input Currency ")
Input_amount=input("Input amount ")
Output_Currency= input("Output Currency ")
s= CurrencyCodes()
sIN=s.get_symbol(Input_Currency)
sOUT=s.get_symbol(Output_Currency)
#print(sIN)
#print(sOUT)
Output_Values=c.get_rates(Input_Currency)
Output_amount=float(Output_Values[Output_Currency])*float(Input_amount)
#print(Output_Values)
#print(len(Output_Values))
list2=[]
i=0
#for i in range(0,33)): 
for x, y in Output_Values.items():
    list2.append(x)
    
    

print(list2)
    


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from pymodbus.client.sync import ModbusSerialClient as Modbusclient
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse
import struct


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("untitled1.ui", self)
        self.pushButton_1.clicked.connect(self.Read_Coil)
        self.pushButton_2.clicked.connect(self.Read_Discrete_Inputs)
        self.pushButton_3.clicked.connect(self.Read_Holding_Register)
        self.pushButton_4.clicked.connect(self.Read_Input_Register)
        self.pushButton_5.clicked.connect(self.Get_Settings)
        self.pushButton_6.clicked.connect(self.Write_Coil)
        self.pushButton_7.clicked.connect(self.Write_Holding_Register)
        self.pushButton_8.clicked.connect(self.Disconnection)
        
        

    def Get_Settings(self):
        self.Ip_Address=self.lineEdit_1.text()
        self.Server_Port=self.lineEdit_2.text()
        self.Slave_ID=int(self.lineEdit_3.text())
        self.Buade_Rate=self.lineEdit_4.text()
        self.Pairty=self.lineEdit_5.text()
        self.Stopbit=self.lineEdit_6.text()
        self.Starting_Address=int(self.lineEdit_7.text())-1
        self.Number_Of_Values=int(self.lineEdit_8.text())
        
        self.client = ModbusClient( self.Ip_Address , port=self.Server_Port)
        connection=self.client.connect()
        if connection == True:
            self.listWidget_2.clear()
            self.listWidget_2.setStyleSheet("background-color : green")
            self.listWidget_2.addItem("Connected To Server")
        
        self.client.close()

    def Disconnection(self):
        self.listWidget_2.clear()
        self.listWidget_2.setStyleSheet("background-color : red")
        self.listWidget_2.addItem("Not Connected To Server")
        self.client.close()
        self.listWidget_1.clear()

    def Read_Coil(self):
        self.Get_Settings()
        #print(self.Starting_Address)
        Coil_value = self.client.read_coils(self.Starting_Address,self.Number_Of_Values,unit=self.Slave_ID)
        #bits to read discrete input and coil
        self.listWidget_1.clear()
        for i in range(0,self.Number_Of_Values):
            self.listWidget_1.addItem(str(Coil_value.bits[i]))
            if i==(self.Number_Of_Values-1): 
                break 
        self.client.close()
        
    def Read_Discrete_Inputs(self):
        self.Get_Settings()
        #print(self.Starting_Address)
        discrete_inputs_value = self.client.read_discrete_inputs(self.Starting_Address,self.Number_Of_Values,unit=self.Slave_ID)
        #bits to read discrete input and coil
        self.listWidget_1.clear()
        for i in range(0,self.Number_Of_Values):
            self.listWidget_1.addItem(str(discrete_inputs_value.bits[i]))
            if i==(self.Number_Of_Values-1): 
                break 
        self.client.close()
        

    def Read_Holding_Register(self):
        self.Get_Settings()
        #print(self.Starting_Address)
        HRegister_value = self.client.read_holding_registers(self.Starting_Address,self.Number_Of_Values,unit=self.Slave_ID)
        #bits to read discrete input and coil
        self.listWidget_1.clear()
        for i in range(0,self.Number_Of_Values):
            self.listWidget_1.addItem(str(HRegister_value.registers[i]))
            if i==(self.Number_Of_Values-1): 
                break 
        self.client.close()

    def Read_Input_Register(self):
        self.Get_Settings()
        #print(self.Starting_Address)
        IRegister_value = self.client.read_input_registers(self.Starting_Address,self.Number_Of_Values,unit=self.Slave_ID)
        #bits to read discrete input and coil
        self.listWidget_1.clear()
        for i in range(0,self.Number_Of_Values):
            self.listWidget_1.addItem(str(IRegister_value.registers[i]))
            if i==(self.Number_Of_Values-1): 
                break 
        self.client.close()
    
    def Write_Coil(self):
        self.Get_Settings()
        Coil_value=self.comboBox_1.currentText()
        Coil_Address=int(self.lineEdit_9.text())-1
        
        if Coil_value == 'True':
            rq = self.client.write_coil(Coil_Address, True*1, unit=self.Slave_ID)
            self.client.close()
        if Coil_value == 'False':
            rq = self.client.write_coil(Coil_Address, False*1, unit=self.Slave_ID)
            self.client.close()


    def Write_Holding_Register(self):
        self.Get_Settings()
        Register_Address=int(self.lineEdit_10.text())-1
        Register_value=int(self.lineEdit_11.text())
        rq = self.client.write_registers(Register_Address, Register_value*1, unit=self.Slave_ID)
        self.client.close()
    
    



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
from pymodbus.client.sync import ModbusSerialClient as Modbusclient
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse
import struct




# For reading Descrete inputs
def Read_Discrete_Inputs(Address,Registers, Slave_Id):
    discrete_inputs_value = client.read_discrete_inputs(Address,Registers,unit=Slave_Id)
    #bits to read discrete input and coil
    for i in range(0,8):
        print(discrete_inputs_value.bits[i])
        if i==(Number_Of_Registers-1): 
            break

def Read_Coil(Address,Registers,Slave_Id):
    Coil_value = client.read_coils(Address,Registers,unit=Slave_Id)
    #bits to read discrete input and coil
    for i in range(0,8):
        print(Coil_value.bits[i])
        if i==(Number_Of_Registers-1): 
            break        

def Read_Holding_Register(Address,Registers,Slave_Id):   
    HRegister_value = client.read_holding_registers(Address,Registers,unit=Slave_Id)
    #registers to read HR and IR
    for i in range(0,8):
        print(HRegister_value.registers[i])
        if i==(Number_Of_Registers-1): 
            break 

def Read_Input_Register(Address,Registers,Slave_Id):  
    IRegister_value  = client.read_input_registers(Address,Registers,unit=Slave_Id)
    #registers to read HR and IR
    for i in range(0,8):
        print(IRegister_value.registers[i])
        if i==(Number_Of_Registers-1): 
            break 

def Write_Coil(Address,Registers, Slave_Id,Coil_command):
    #Coil_value = client.write_coil(Address, Coil_command*1, unit=Slave_Id)
    list1=Coil_command.split(",")
    list_length=len(list1)

    for i in range(0,list_length):  
        if list1[i]== 'True':
            list1[i]=True
        elif list1[i]== 'False':
            list1[i]=False
    list_length=len(list1)
    for i in range(0,list_length):
        rq = client.write_coil(Address+i, list1[i]*1, unit=Slave_Id)
      
def Write_HRegister(Address,Registers, Slave_Id,HRegister_command):
    #Coil_value = client.write_coil(Address, Coil_command*1, unit=Slave_Id)
    list1=HRegister_command.split(",")
    list_length=len(list1)
    for i in range(0,list_length):
        Value=int(list1[i])
        rq = client.write_registers(Address+i, Value*1, unit=Slave_Id)


Modbus_Protocol= input('TCP or RTU ')

while 1:
    print("In"+Modbus_Protocol.upper()+"Mode")
    
    if Modbus_Protocol.upper()=='RTU':
        Com_port= input('Com_port ')
        Baudrate= int(input('Baudrate '))
        client=Modbusclient(method='rtu',port='COM4',stopbits=1,bytesize=8,baudrate=9600,timeout=0.3)
        connection=client.connect()
        print(connection)

    if Modbus_Protocol.upper()=='TCP':
        IP= input('Ip Address ')
        Port= int(input('Port '))
        client = ModbusClient( IP , port=Port)
        connection=client.connect()
        print(connection)

    Register_Read=input("""
RC -- Read Coil 
RD -- Read Discrete Input 
RH -- Read Holding Register
RI -- Read Input Register
WC -- Write Coil
        """
          )

       
    Starting_Address=int(input('Enter starting register '))-1
    Number_Of_Registers=int(input('Enter no of register '))
    Slave_Id=int(input('Enter Slave id '))

    if Register_Read.upper()=='RD':
        Read_Discrete_Inputs(Starting_Address,Number_Of_Registers,Slave_Id)
        
    if Register_Read.upper()=='RC':
        Read_Coil(Starting_Address,Number_Of_Registers,Slave_Id)

    if Register_Read.upper()=='RH':
        Read_Holding_Register(Starting_Address,Number_Of_Registers,Slave_Id)

    if Register_Read.upper()=='RI':
        Read_Input_Register(Starting_Address,Number_Of_Registers,Slave_Id)
    
    if Register_Read.upper()=='WC':
        print("True or False Enter Values seprated by ','")
        Coil_command= input()
        Write_Coil(Starting_Address,Number_Of_Registers,Slave_Id,Coil_command)
   
    if Register_Read.upper()=='WHR':
        print("Enter Values seprated by ','")
        HRegister_command= input()
        Write_HRegister(Starting_Address,Number_Of_Registers,Slave_Id,HRegister_command)
    
    
    Exit=input('Exit  y/n ')
    client.close()
    if Exit.upper()=='Y':
        print('Exit')
        break
client.close()
    
# --------------------------------------------------------------------------- #
# Tarea programada windows segun https://blogs.esri.com/esri/arcgis/2013/07/30/scheduling-a-scrip/
# --------------------------------------------------------------------------- # 
from pymodbus.client.sync import ModbusTcpClient

# --------------------------------------------------------------------------- # 
# configure the client logging
# --------------------------------------------------------------------------- # 
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# --------------------------------------------------------------------------- # 
# configure BBDD
# instalar como administrador en Windows: pip install mysql-connector-python
# --------------------------------------------------------------------------- # 
import mysql.connector as my_dbapi

# --------------------------------------------------------------------------- # 
# Descripcion de zonas de memoria
# TCP2RS modbus TCP:
#   - http://www.intesiscon.com/ficheros/manuales-tecnicos/73-M54032-TPC2RS-MODBUSTCP.pdf
# CVM-K
#   - http://www.convert.com.pl/docs/instrukcje/CVMk-H_en.pdf
# --------------------------------------------------------------------------- # 

# --------------------------------------------------------------------------- # 
# Instalar pymodbus: pip install pymodbus
# get data from modbus
# --------------------------------------------------------------------------- #

'''
#scan zonas de memoria
for x in range (1000):
    try:
        result = client.read_holding_registers(x, 1)
        print(str(x) + "-" + str(hex(x)) + " -->" + str(result.registers))
    except:
        y = 0
'''

# Pruebas lecturas y maximos en los modelos CVM-K (el maximo no funciona)
client_CG = ModbusTcpClient('192.168.1.11', port=502, timeout=10)
client_CG.connect()
log.debug("Reading Registers")

for j in range(100):
    result = client_CG.read_holding_registers(0x2a, 2, unit = 1)
    result_max = client_CG.read_holding_registers(0x44, 2, unit = 1)
    dato = ((result.registers[0]*65535) + result.registers[1])/1000
    dato_max = ((result_max.registers[0]*65535) + result_max.registers[1])/1000
    print(str(j) + " --> " + str(result.registers) + " - " + str(dato)+ " -- " +str(result_max.registers)\
          + " - " + str(dato_max))
client_CG.close()

# Pruebas lecturas y máximo en modelo CVM-144
client_GS = ModbusTcpClient('192.168.1.12', port=502, timeout=10)
client_GS.connect()
log.debug("Reading Registers")

for j in range(100):
    result = client_GS.read_holding_registers(0x1e, 2)
    result_max = client_GS.read_holding_registers(0x7e, 2)
    dato = ((result.registers[0]*65535) + result.registers[1])/1000
    dato_max = ((result_max.registers[0]*65535) + result_max.registers[1])/1000
    print(str(j) + " --> " + str(result.registers) + " - " + str(dato)+ " -- " +str(result_max.registers)\
          + " - " + str(dato_max))
client_GS.close()

# Prueba scan de un módulo TCP2RS modbus module para medidores CVM-K conectados en bus modbus
monitor_energia = {'ip':'192.168.1.10','power': 0,'max_power':0}

client = ModbusTcpClient(monitor_energia['ip'], port=502, timeout=10)
client.connect()
log.debug("Reading Registers")
result = client.read_holding_registers(0, 82) #dirección inicio, numero bytes a leer. Solo del dispositivo 0
print(result.registers) #imprimo todo

# Para seleccionar otro dispositivo del bus, usar la variable unit de la función read_holding_registers
# CUANDO SE USAN LOS DOS BYTES ES: PRIMER BYTE * 65535 + SEGUNDO BYTE (correspondinete a codificacion de 16 bits)

for i in range (0,600,2):
    try:
        result = client.read_holding_registers(i, 2, unit = 4)	#unidad 4 conectada al TCP2RS modbus module 
        dato = ((result.registers[0]*65535) + result.registers[1])/1000
        print(str(i) + " --> " + str(result.registers) + " - " + str(dato))
    except:
        pass

monitor_energia['power'] = client.read_holding_registers(42, 2, unit = 1).registers	#Potencia Trifasica W unidad 1
print("unidad 1 --> Power = " + str(monitor_energia['power']))

monitor_energia['power'] = client.read_holding_registers(42, 2, unit = 3).registers	#Potencia Trifasica W unidad 3
print("unidad 3 --> Power = " + str(monitor_energia['power']))

monitor_energia['power'] = client.read_holding_registers(42, 2, unit = 4).registers	#Potencia Trifasica W unidad 4
print("unidad 4 --> Power = " + str(monitor_energia['power']))

monitor_energia['power'] = client.read_holding_registers(42, 2, unit = 5).registers	#Potencia Trifasica W unidad 5
print("unidad 5 --> Power = " + str(monitor_energia['power']))

client.close()
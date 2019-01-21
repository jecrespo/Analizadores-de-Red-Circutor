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
# get data from modbus
# descripcion zonas memoria http://www.convert.com.pl/docs/instrukcje/CVM-144-ETH-TCP_en.pdf
# --------------------------------------------------------------------------- #
client = ModbusTcpClient('192.168.0.10', port=502, timeout=10)
client.connect()
log.debug("Reading Registers")
result = client.read_holding_registers(0, 4)    #dirección inicio, numero bytes a leer
print(result.registers)
potencia_trifasica = client.read_holding_registers(0x1e, 2)
print(potencia_trifasica.registers)
client.close()

cnx_my = my_dbapi.connect(user='miusuario', password='mipassword', host='192.168.1.10', database='Circutor')
cursor_my = cnx_my.cursor()
query_my = "INSERT INTO mitabla (Consumo) VALUES (" + str(potencia_trifasica.registers[1]) + ")"
cursor_my.execute(query_my)
cnx_my.commit()
cnx_my.close()

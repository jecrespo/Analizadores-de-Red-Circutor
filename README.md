# Analizadores de Red Circutor

Obtener Datos de un Equipo Circutor Mediante Modbus TCP usando librería pymodbus de Python y guardar en una base de datos.

Analizadores probados:
* Power meter Circutor CVM-144 http://circutor.es/docs/FT_M5_CVM144_SP.pdf
<img src="http://circutor.es/images/stories/virtuemart/product/FO_CVM144_250x250.jpg" width="250" height="250" />
* Power meter Circutor CVM-K (no dispone de ethernet) + TCP2RS modbus module
<img src="http://www.ulrichmatterag.ch/shop/contents/media/circutor_analys_cvmk.gif" width="250" height="250" />

Manual con las zonas de memoria de cada dispositivo:
* http://www.convert.com.pl/docs/instrukcje/CVM-144-ETH-TCP_en.pdf 
* http://www.convert.com.pl/docs/instrukcje/CVMk-H_en.pdf
* http://www.convert.com.pl/docs/instrukcje/CVMk-HAR_en.pdf 

###Pymodbus
**pymodbus** es una librería de python para conectar con dispositivos modbus

Enlaces:
* Web: https://pypi.python.org/pypi/pymodbus
* Documentación: https://pymodbus.readthedocs.io/en/latest/ 
* Github: https://github.com/riptideio/pymodbus/

Con el método read_holding_registers de pymodbus es posible leer los registros de un dispositivo.

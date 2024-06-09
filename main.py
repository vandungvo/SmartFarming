import Utilities.modbus485
import serial as serial
import time

try:
    ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
except:
    print("Modbus485 - Failed to open serial port")

modbus485 = Utilities.modbus485.Modbus485(ser)

relay1_ON  = [1, 6, 0, 0, 0, 255, 201, 138]
relay1_OFF = [1, 6, 0, 0, 0, 0, 137, 202]

relay2_ON  = [2, 6, 0, 0, 0, 255, 201, 185]
relay2_OFF = [2, 6, 0, 0, 0, 0, 137, 249]

relay3_ON  = [3, 6, 0, 0, 0, 255, 200, 104]
relay3_OFF = [3, 6, 0, 0, 0, 0, 136, 40]

relay4_ON  = [4, 6, 0, 0, 0, 255, 201, 223]
relay4_OFF = [4, 6, 0, 0, 0, 0, 137, 159]

relay5_ON  = [5, 6, 0, 0, 0, 255, 200, 14]
relay5_OFF = [5, 6, 0, 0, 0, 0, 136, 78]

relay6_ON  = [6, 6, 0, 0, 0, 255, 200, 61]
relay6_OFF = [6, 6, 0, 0, 0, 0, 136, 125]

relay7_ON  = [7, 6, 0, 0, 0, 255, 201, 236]
relay7_OFF = [7, 6, 0, 0, 0, 0, 137, 172]

relay8_ON  = [8, 6, 0, 0, 0, 255, 201, 19]
relay8_OFF = [8, 6, 0, 0, 0, 0, 137, 83]

soil_temperature = [10, 3, 0, 6, 0, 1, 101, 112]
soil_humidity = [10, 3, 0, 7, 0, 1, 52, 176]

modbus485.modbus485_send(soil_temperature)
time.sleep(1)
print(modbus485.modbus485_read_adc() / 100)

modbus485.modbus485_send(soil_humidity)
time.sleep(1)
print(modbus485.modbus485_read_adc() / 100)

modbus485.modbus485_send(relay1_ON)
time.sleep(1)
modbus485.modbus485_send(relay1_OFF)
time.sleep(1)
modbus485.modbus485_send(relay2_ON)
time.sleep(1)
modbus485.modbus485_send(relay2_OFF)
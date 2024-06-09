import Utilities.controller
from Adafruit_IO import MQTTClient
import Utilities.connect
import Utilities.controller
import time
import Utilities.modbus485

controller = Utilities.controller.Controller()

client = MQTTClient(Utilities.connect.AIO_USERNAME , Utilities.connect.AIO_KEY)
client.on_connect = Utilities.connect.Connection.connected
client.on_subscribe = Utilities.connect.Connection.subscribe
client.on_disconnect = Utilities.connect.Connection.disconnected
client.on_message = Utilities.connect.Connection.message

client.connect()
client.loop_background()

while True:
    Utilities.modbus485.Modbus485.modbus485_read()
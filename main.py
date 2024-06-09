import Utilities.controller

controller = Utilities.controller.Controller()

print(controller.readTemperature())
print(controller.readHumidity())

controller.controlMixer1("ON")
controller.controlMixer2("ON")
controller.controlMixer3("ON")
controller.controlPumpIn("ON")

controller.controlMixer1("OFF")
controller.controlMixer2("OFF")
controller.controlMixer3("OFF")
controller.controlPumpIn("OFF")

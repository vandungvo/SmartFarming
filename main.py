import Utilities.controller

controller = Utilities.controller.Controller()

print(controller.readTemperature())
print(controller.readHumidity())

controller.controlMixer1("ON")
controller.controlMixer2("ON")
import Utilities.controller as controller

controller = controller.Controller()

print(controller.readTemperature())
print(controller.readHumidity())

print(controller.controlMixer1("ON"))
print(controller.controlMixer2("ON"))

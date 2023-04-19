from p110 import P110Controller
from l530 import L530Controller

class Device:
    def __init__(self, log, device, config):
        self.log = log
        if 'p110' in device:
            self.controller = P110Controller(log, device, config)
        elif 'l530' in device:
            self.controller = L530Controller(log, device, config)

    def action(self, action):
        self.controller.action(action)
            


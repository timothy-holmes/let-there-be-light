from p110 import P110Controller

class Light:
    def __init__(self, log, device, config):
        self.log = log
        self.controller = P110Controller(log, device, config)

    def action(self, action):
        self.log.debug(self.controller.action(action_str=action))

        if not action == 'getDeviceInfo':
            self.log.debug(self.controller.action(action_str='getDeviceInfo'))


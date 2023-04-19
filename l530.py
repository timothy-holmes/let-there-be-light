from PyP100 import PyL530


class L530Controller:
    def __init__(self, log, device, config):
        self.device = device
        self.config = config
        self.log = log

    def _authenticate(self):
        try:
            _ = self.obj.getDeviceInfo()
        except Exception as e1:
            try:
                self.obj = PyL530.L530(
                    self.device, 
                    self.config['DEVICE_USER'], 
                    self.config['DEVICE_PASSWORD']
                )
                self.obj.handshake()
                self.obj.login()
            except Exception as e2:
                e = f"L530 Authentication Error (L1): {e2}"
                self.log.error(e)
            try:
                _ = self.obj.getDeviceInfo()
            except Exception as e3:
                e = f"L530 Authentication Failed (L2): {e3}"
                self.log.error(e)
        
    def action(self,action_str: str) -> str:
        allowed_methods = [
            'turnOn-red',
            'turnOn-blue',
            'turnOff'
        ]
        colors = {
            'red': 0,
            'blue': 240
        }
        if not action_str in allowed_methods:
            return 'Method not allowed'
        
        try:
            getattr(self.obj,action_str)()
            if '-' in action_str:
                self.obj.setBrightness(100)
                self.obj.setColor(colors[action_str.split('-')[1]],100)
        except Exception as e1:
            self._authenticate()
            getattr(self.obj,action_str)()
            if '-' in action_str:
                self.obj.setBrightness(100)
                self.obj.setColor(colors[action_str.split('-')[1]],100)
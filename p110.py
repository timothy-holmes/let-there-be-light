from PyP100 import PyP110


class P110Controller:
    def __init__(self, log, device, config):
        self.device = device
        self.config = config
        self.log = log

    def _authenticate(self):
        try:
            _ = self.obj.getDeviceInfo()
        except Exception as e1:
            try:
                self.obj = PyP110.P110(
                    self.device, 
                    self.config['DEVICE_USER'], 
                    self.config['DEVICE_PASSWORD']
                )
                self.obj.handshake()
                self.obj.login()
            except Exception as e2:
                e = f"P110 Authentication Error (L1): {e2}"
                self.log.error(e)
            try:
                _ = self.obj.getDeviceInfo()
            except Exception as e3:
                e = f"P110 Authentication Failed (L2): {e3}"
                self.log.error(e)

    def action(self,action_str: str) -> str:
        allowed_methods = [
            'turnOn',
            'turnOff',
            'getDeviceInfo',
            'getEnergyUsage'
        ]
        if not action_str in allowed_methods:
            return 'Method not allowed'
        try:
            return getattr(self.obj,action_str)()
        except Exception as e1:
            self._authenticate()
            return getattr(self.obj,action_str)()
import argparse
from os import environ as ENV_VARS

from logger import log
from device import Device

def main(action,devices):
    for device in devices:
        ltbl = Device(log=log, device=device, config=ENV_VARS)
        ltbl.action(action)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--action', 
        dest='action', 
        #type=str, 
        help='Perform action: turnOn, turnOff, getDeviceInfo, getEnergyUsage, turnOn-blue, turnOn-red'
    )
    parser.add_argument(
        '--devices', 
        dest='devices', 
        #type=str,
        nargs='+',
        help='Specify one or more devices: p110-[desk,couch,kallax].iot.home'
    )
    args = parser.parse_args()
    main(args.action,args.devices)

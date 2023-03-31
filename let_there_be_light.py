import argparse
from os import environ as ENV_VARS

from logger import log
from light import Light

def main(action):
    ltbl = Light(log=log, config=ENV_VARS)
    ltbl.action(action)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--action', 
        dest='action', 
        type=str, 
        help='Perform action: turnOn, turnOff, getDeviceInfo, getEnergyUsage'
    )
    args = parser.parse_args()
    main(args.action)

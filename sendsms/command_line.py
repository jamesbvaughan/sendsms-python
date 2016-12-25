from configparser import ConfigParser
from sendsms import sendSMS, getConfig


def main():
    config = getConfig()
    my_number = config['General']['MY_NUMBER']

    sendSMS(input(), my_number)

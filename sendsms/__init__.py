from twilio.rest import TwilioRestClient
from configparser import ConfigParser
from os import path, makedirs


def getConfig():
    homeDir = path.expanduser('~')
    configFilename = path.join(homeDir, '.config/sendsms/config')

    # Make the config directory if it doesn't exist
    makedirs(path.dirname(configFilename), exist_ok=True)

    config = ConfigParser()
    config.read(configFilename)
    return config


def sendSMS(body, number):
    config = getConfig()
    account_sid = config['Twilio']['ACCOUNT_SID']
    auth_token = config['Twilio']['AUTH_TOKEN']
    twilio_number = config['Twilio']['TWILIO_NUMBER']

    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(body=body, to=number, from_=twilio_number)

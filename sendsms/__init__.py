from twilio.rest import TwilioRestClient
from configparser import ConfigParser

def sendSMS(body):
    config = ConfigParser()
    config.read('config.sample')
    account_sid = config['Twilio']['ACCOUNT_SID']
    auth_token = config['Twilio']['AUTH_TOKEN']
    twilio_number = config['Twilio']['TWILIO_NUMBER']
    my_number = config['General']['MY_NUMBER']

    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(body=body, to=my_number, from_=twilio_number)

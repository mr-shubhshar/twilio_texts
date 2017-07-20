from twilio.rest import Client
from credentials import account_sid, auth_token, my_ph, my_twilio_ph

client = Client(account_sid, auth_token)

msg = "Test msg sent from Python"

message = client.messages.create(to=my_ph, from_=my_twilio_ph, body=msg)

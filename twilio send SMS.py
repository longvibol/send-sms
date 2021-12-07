from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG432dcf6ecc634c360a6db32123120d6c',
    body='Bong Testing te Hhehe ',
    to='+'
)

print(message.sid)

# https://console.twilio.com/us1/develop/sms/try-it-out/send-an-sms?frameUrl=%2Fconsole%2Fsms%2Fgetting-started%2Fbuild%3Fx-target-region%3Dus1
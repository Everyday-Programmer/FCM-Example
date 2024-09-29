import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate('firebase_cred.json')

firebase_admin.initialize_app(cred)

def send_fcm_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token
    )

    try:
        response = messaging.send(message)
        print('Notification sent successfully!', response)
    except Exception as e:
        print('Error sending notification: ', e)

token = '' # Paste the device token here
send_fcm_notification(token, 'Test notification!', 'Hello from python firebase admin SDK')

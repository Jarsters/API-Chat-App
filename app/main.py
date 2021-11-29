from flask import Flask, request as req

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
import json
import datetime

cred = credentials.Certificate("rnchatapplication-firebase-adminsdk-mo55t-5ee1e63565.json")
# cred = credentials.Certificate("C:\\Users/Asus/Downloads/appchat-3e29e-firebase-adminsdk-eoph8-d76544aa6e.json")
app = firebase_admin.initialize_app(cred)
contoh_token = 'ciE5Vo8YRkyACyACnfTq_h:APA91bFGY4Hu-DF_FkpRltbe-D_kiGkCDM1tSMmIkgTGpZu_C9W_OC3bY6QOkuBmSIYPDka4_RZ0TXi2_R-QTaFw87Q6MrKPXUxP9CtUpNufwzr0GxfP2VyDolh6hXrtsadXCqd7JTV2'
# contoh_token2 = 'eK6PIHsfS9KQaaIM6KZmIX:APA91bGtMxq4yOphQuIBWulZoy0F7ISeNIOOASmqMEHe0STSWOSheeMTNfgq39SeAYH9kjIoB0unXZcJ5Rd5myDq4uz6srMdnQmB6fx9xlgcgldnrUXHF6NpVaYuP9CEqA-oVkiskl5t'

appf = Flask(__name__)

@appf.route('/')
def index():
    return "<h1>Hello World!</h1>"

@appf.route("/send-message-token", methods=['POST'])
def send_message():
    data_json = req.get_json(force=True)
    token = data_json.get('token') if data_json.get('token') else 'ciE5Vo8YRkyACyACnfTq_h:APA91bFGY4Hu-DF_FkpRltbe-D_kiGkCDM1tSMmIkgTGpZu_C9W_OC3bY6QOkuBmSIYPDka4_RZ0TXi2_R-QTaFw87Q6MrKPXUxP9CtUpNufwzr0GxfP2VyDolh6hXrtsadXCqd7JTV2'
    message = data_json['message']
    title = data_json['title']
    data = data_json['data']
    # time = data_json['time']
    # img = data_json['imagebase64']
    message = messaging.Message(
        notification=messaging.Notification(
            # title='Something New Coming!',
            title=title,
            body=message,
        ),
        # android=messaging.AndroidConfig(
        #     ttl=datetime.timedelta(seconds=3),
        #     priority='high',
        #     notification=messaging.AndroidNotification(
        #         icon='stock_ticker_update',
        #         color='#f45342'
        #     ),
        # ),
        data=data,
        token=token,
    )
    resp = messaging.send(message)
    print(data)
    print(resp)
    return {"Response: ": resp, 'data':data, 'Status':"Success"}
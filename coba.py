from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Vn5EbjcYn3OF4FhiOBL5OGDBZubbNCC+5ko4eNWaI2SLGqkjOesHswAmNiAVeQn6ij97tLnNn6gTaPIg8Cw8jIMoaCQPLQTd+NI+E9lork6vsFHVFIvV569Vyq1UyA0ekcF4rd5UENsYnVzghfKrjQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0d210d474a538b26e597646133fad0f1')

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        print(body)
        print(signature)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event.reply_token)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()

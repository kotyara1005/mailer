import requests
from flask import Flask, request

DOMAIN = 'sandboxcd1af7b6f36a478fb4dad6c5686ac6df.mailgun.org'
API_KEY = '7b54d6f7fd7d19b9c13d4a525f21d3a8-a3d67641-f101c0dd'

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def send_main():
    if request.method == 'POST':
        resp = requests.post(
            "https://api.mailgun.net/v3/{}/messages".format(DOMAIN),
            auth=("api", API_KEY),
            data={"from": "Excited User <mailgun@{}>".format(DOMAIN),
                  "to": ["krivonosaa1994@yandex.ru"],
                  "subject": "Hello",
                  "text": "Testing some Mailgun awesomness!\nTest link: http://bb13ddd8.ngrok.io/api/test/"}
        )
        if resp.ok:
            return 'OK'
        else:
            return 'ERROR \n{}'.format(resp.text)
    else:
        return '''<form method="POST"><button type="submit">Send</button></form>'''


@app.route('/api/webhook/', methods=('POST',))
def webhook():
    print(request.data)
    return ''


@app.route('/api/test/')
def test():
    return 'test'


if __name__ == '__main__':
    app.run()

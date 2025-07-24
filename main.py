
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ ربات فعال است!'

@app.route('/receiveUpdate', methods=['POST'])
def receive_update():
    data = request.json
    print("📩 پیام دریافتی:", data)
    return {'status': 'received'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_key', methods=['POST'])
def receive_key():
    key = request.form['key']
    with open('received_keys.txt', 'a') as f:
        f.write(key + '\n')
    return 'Kunci diterima', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
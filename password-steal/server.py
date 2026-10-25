from flask import Flask, request

app = Flask(__name__)

@app.route('/capture', methods=['POST'])
def capture():
    data = request.form['data']
    with open('captured_data.txt', 'a') as f:
        f.write(data + '\n')
    return 'Data received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
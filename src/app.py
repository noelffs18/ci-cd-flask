from flask import Flask

PORT = 8000



app = Flask(__name__)

@app.route('/noel')
def hello():
    return "Hola soy noel"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
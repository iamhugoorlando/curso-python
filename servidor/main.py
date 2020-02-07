from flask import Flask

app = Flask(__name__)


@app.route('/')
def hola_mundo():
    return 'Hola Mundo en Flask y Python'


if __name__ == '__main__':
    app.run()

# -*- coding: utf-8 -*-

from simple_flask import SimpleFlask

app = SimpleFlask(__name__)

@app.route('/')
def hello():

    return 'hello world!'

if __name__ == '__main__':
    app.run()

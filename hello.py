# -*- coding: utf-8 -*-

from simple_flask import SimpleFlask

app = SimpleFlask()

@app.route('/')
def hello():

    return 'hello world!'

if __name__ == '__main__':
    app.run()

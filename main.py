import io
import struct
import logging
import datetime

from flask import Flask, Response, abort, render_template, flash, request, redirect, url_for

app = Flask(__name__,
    static_url_path='',
    static_folder='static',)

app.config['WTF_CSRF_ENABLED'] = True

app.secret_key = 'ntqQBTlDG9ExRrnR2byo'


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000', debug=False)
import os
import glob
from datetime import datetime
from csv import reader
import pandas as pd
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, flash
from werkzeug.utils import secure_filename
from multiprocessing import Process
from gevent.pywsgi import WSGIServer

from controllers import text, preprocess

UPLOAD_FOLDER = './data/'

app = Flask(__name__)

print('Model loaded. Check http://127.0.0.1:3000/')


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/form', methods=['GET', 'POST'])
def upload_file():
    global final
    if request.method == 'POST':
        form_data = request.form.get('form_data')
        print(form_data)
        form_data = [form_data]
        #cleaned_data = preprocess.preprocess(form_data)
        #print(cleaned_data)
        final = text.text_classification(form_data)
        print(final)

    return render_template('base.html', result=final)


if __name__ == '__main__':
    # app.run(port=5002, threaded=False)
    Debug =True
    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 3000), app)
    http_server.serve_forever()




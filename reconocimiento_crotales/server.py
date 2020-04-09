import os
import tempfile

from flask import Flask, render_template, request
from waitress import serve

from reconocimiento_crotales.PretrainedReader import PretrainedReader

app = Flask(__name__)
reader = PretrainedReader()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img = request.files['image']
        _, path = tempfile.mkstemp()
        img.save(path)
        identifier = reader.process_image(path)
        return render_template('index.html', result=identifier)
    return render_template('index.html', result=None)


if __name__ == "__main__":
   serve(app, host='0.0.0.0', port=8000)

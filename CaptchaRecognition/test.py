from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

import os


app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.join('/home/yanzhengbin/Training-17b-2015/CaptchaRecognition/')
        upload_path = os.path.join(basepath,'image',secure_filename(f.filename))

        f.save(upload_path)
        return render_template("upload.html")
    return render_template("index.html")
@app.route('/result')
def result():
    
    with open("data/yanzhengbin.txt","rt")as f:
        a = f.readlines()
    return render_template('result.html',result=a)

if __name__ == '__main__':
    app.run(debug=True)
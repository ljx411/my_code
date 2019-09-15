import os

import flask
from flask import render_template, request, redirect, url_for
from flask import app

app = app.Flask(__name__)


@app.route('/')
def get():
    return '你好'


@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method == 'POST':
        f = request.files.getlist('file')
        for t in f:
            t.save(r'E:\yuner\\' + t.filename)
        return redirect(url_for('image'))
        # for t in f:
        #     print(t)
        # f.save(r'E:\芸儿\\' + f.filename)
    return render_template('image.html')


@app.route('/<int:id>/imagepage', methods=['GET', 'POST'])
def image_page(id):
    path_image = r'E:/my_code/flask_demo/static/yuner/'
    files = os.listdir(path_image)
    if id == len(files):
        id = 0
    file = os.path.join('/static/yuner/' + files[id])
    return render_template('image_page.html', file=file, id=id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # print(os.path.dirname(__file__))

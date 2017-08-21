# coding=utf8
# !/usr/bin/python
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'



@app.route('/',methods = ['GET' , 'POST'])
def login():
    #接收参数
    print "t"
    #提交验证
    if request.method == "POST":
        a = request.get_data() #ajx 提交的json 数据
        print a[1]
        dict1 = json.loads(a)
        print dict1
    return render_template('login.html')

@app.route('/index',methods = ['GET' , 'POST'])
def index():
    print "index"
    if request.method == "POST":
        print('username:' + str(request.form.get("username")) + ',password:' + request.form.get("password")) #表单提交的数据

        return render_template('index.html', username=request.form['username'], liu="ttt", jian="qqqq")
    else:
        return "404"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
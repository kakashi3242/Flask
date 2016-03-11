from flask import Flask, url_for, request, render_template
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)

# 静态路由
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/hello')
def hello():
    return 'Hello world!'

# 动态URL路由
@app.route('/hi/<username>')
def user(username):
   return '<h1>Hello %s!</h1>' % username

@app.route('/int/<int:username>')
def user_int(username):
    return 'User int %d' % username


# 构造URL  ????
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('user_int', username = 23333))





if __name__ == '__main__':
    # 启动调试模式,修改后不需要重新运行代码
    # 1.
    app.debug = True
    app.run()

    manager.run()
    # 2.
    # app.run(debug = True)

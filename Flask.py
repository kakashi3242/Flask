from flask import Flask

app = Flask(__name__)

# 静态路由
@app.route('/')
def index():
    return 'Index page!'

@app.route('/hello')
def hello():
    return 'Hello world!'

# 动态URL路由
@app.route('/hi/<username>')
def user(username):
    return 'User %s' % username




if __name__ == '__main__':
    # 启动调试模式,修改后不需要重新运行代码
    # 1.
    app.debug = True
    app.run()
    # 2.
    # app.run(debug = True)

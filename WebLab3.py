from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Добавьте в поисковой строке: /user/желаемое имя<h1>'

@app.route('/user/<username>')
def show_user_profile(username):
    return '<h1>User %s<h1>' % username


if __name__ == '__main__':
    app.run()
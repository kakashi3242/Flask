import os

from flask import render_template, Flask, session, redirect, url_for,flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from mysql import insert, query


# ...

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'hard to guess string'

app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)

    users = db.relationship('User', backref = 'role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        _name = query(form.name.data)
        flash('Hello, %s' % _name)
        # insert(form.name.data)
        return redirect(url_for('index'))
    return render_template('index.html', form = form, name = session.get('name'))



# @app.route('/user/list')
# def user():
#     mydict = ['key', 'value', 'name', 'mmar']
#     return render_template('test.html', comments = mydict)

# @app.route('/user/<username>')
# def usr(username):
#     form = NameForm()
#     return render_template('index.html', name = username, form = form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug = True)
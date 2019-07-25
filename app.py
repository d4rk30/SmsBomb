from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import msg_attack

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd4rk30'
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)

class NameForm(FlaskForm):
	phone = StringField('Please enter the phone number to be attacked',validators = [Required()])
	submit = SubmitField('Submit')


@app.route('/',methods = ['GET','POST'])
def index():
	phone = None
	form = NameForm()
	if form.validate_on_submit():
		phone = form.phone.data
		attackobject = msg_attack.AttackObject(phone)
		print(attackobject.phone)
		attackobject.init_data()
	return render_template('index.html',form = form)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404


@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

if __name__ == '__main__':
	manager.run()

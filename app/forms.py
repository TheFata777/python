from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')
	
class CreateForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	text = TextAreaField('Text', validators=[DataRequired()])
	submit = SubmitField('Push')
	
class DeleteForm(FlaskForm):
	submit2 = SubmitField('Delete')
	

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Get Results')

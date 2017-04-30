from flask_wtf import Form
from werkzeug.datastructures import MultiDict
from wtforms import StringField, TextAreaField, SubmitField, validators, ValidationError, PasswordField


class SignupForm(Form):
    name = StringField('Name:', validators=[validators.required()])
    email = StringField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = StringField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

    def reset(self):
        blankData = MultiDict([('csrf', self.reset_csrf())])
        self.process(blankData)
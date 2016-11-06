from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators

def CheckNameLength(form, field):
  if len(field.data) < 4:
    raise ValidationError('Name must have more then 3 characters')

class ContactForm(Form):
    name = StringField([validators.DataRequired(), CheckNameLength])
    email = StringField([validators.DataRequired(), validators.Email('your@codcompsci.club')])
    submit = SubmitField('Send Message')
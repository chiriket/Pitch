from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title',validators=[Required()])
    category = SelectField('Type',choices=[('Interview','Interview'), ('Product','Product'), ('Promotion','Promotion'), ('Business','Business'), ('Tech','Tech')],validators=[Required()])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comments = TextAreaField('Add your Comments', validators=[Required()])
    submit = SubmitField('Submit Comment')  
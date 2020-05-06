from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class AddPitch(FlaskForm):
    title=TextAreaField("Pitch Title",validators=[Required()])
    # category=TextAreaField("Category",validators=[Required()])
    category=RadioField("Category",choices=[("general","General"),("pickuplines","Pick Up Lines"),("Interview Pitch","Interview Pitch"),("Product Pitch","Product Pitch"),("promotion","Promotion")])
    description=TextAreaField("Description",validators=[Required()])
    submit=SubmitField('Submit')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField ,BooleanField, IntegerField, DateField, validators, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo




class RegistrationForm(FlaskForm):

    firstname = StringField('First_name', validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Last_name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')
    
class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class WtinputForm1(FlaskForm):

    # date = DateField('Date', format='%m/%d/%Y', validators=[DataRequired()])
    date = DateField('Date', format='%m/%d/%Y')
    illness = StringField('Illness')
    fatigue = IntegerField('Fatigue Level(0~5)', [validators.NumberRange(0,5, "invalid number")])
    workoutname = StringField('Wokout Name', id = 'livebox')
    weight = IntegerField('Weight(Kg)', default=0)
    workouthours = IntegerField('Workout Hours', default=0)
    set = IntegerField('Set', default=0)
    rep = IntegerField('Rep',  default=0)
    equipment = StringField('Equipment')
    muscleMajor = StringField('Major Muscle', id = 'livebox2')
    muscleMinor = StringField('Minor Muscle')

    sleephours = IntegerField('Sleep Hours', default=0)
    amount = IntegerField('Amount of Water(L)', default=0)
    fooddrinkname = StringField('Food Name')
    carb = IntegerField('Carbonate(g)', default=0)
    protein = IntegerField('Protein(g)', default=0)
    fat = IntegerField('Fat(g)', default=0)
    submit = SubmitField('Save Daily Workout Log', id ='submit1')
    add1 = SubmitField('Add Workout', id = 'add1')
    add2 = SubmitField('Add Nutrition', id ='add2')

    
class UpdateAccountForm(FlaskForm):

    firstname = StringField('Username' ,id = "firstname1")
    email = StringField('Email' ,id = "firstname")
    age = IntegerField('Age', default=0 ,id = "firstname1")
    gender = StringField('Gender', default='Null' ,id = "firstname1")
    bodyweight =  IntegerField('Body Weight(Kg)', default=0 ,id = "firstname1")
    height =  IntegerField('Height(cm)', default=0 ,id = "firstname1")
    submit = SubmitField('Update Personal Profile')



class WtoutputForm(FlaskForm):

    nameSelect = SelectField(u'Workout Name', [DataRequired()], default='1')
    periodSelect = SelectField('Period', [DataRequired()], default='90')
    submit = SubmitField('Select Workout Name and Period', id ='submit2')

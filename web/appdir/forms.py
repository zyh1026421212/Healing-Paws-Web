from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, RadioField, FileField, DateTimeField, TextAreaField, RadioField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange
from flask_wtf.file import FileRequired, FileAllowed

class LoginForm(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegisterForm_C(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()]) # 这里加了一个Email检测器，可以判断是否符合email格式，就不用在前端写js代码检测了
	phone = StringField('Phone', validators=[DataRequired()])
	dob = DateField('Date of Birth (format: YYYY-MM-DD)', format='%Y-%m-%d', validators=[DataRequired()])
	address = StringField('Address', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired()])
	accept_rules = BooleanField('I accept the site rules', validators=[DataRequired()])
	submit = SubmitField('Register')

class RegisterForm_E(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired()])
	loc = SelectField(
        validators=[DataRequired('请选择注册医院所在地')],
        choices=[(1, '北京'), (2, '上海'), (3, '成都')],
        coerce=int
    )
	intro = StringField('Introduction')
	# 暂时没必要，后面可修改得更合理，比如只有用户注册时会显示这个。
	accept_rules = BooleanField('I accept the site rules', validators=[DataRequired()])
	submit = SubmitField('Register')

class AppointmentForm(FlaskForm):
	pet = SelectField(label='为哪只宠物预约', validators=[DataRequired('请选择宠物')], coerce=int)
	loc = RadioField(
        validators=[DataRequired('请选择就医所在地')],
        choices=[(1, '北京'), (2, '上海'), (3, '成都')],
        coerce=int
    )
	is_emergency = RadioField(label='What type of appointment?', choices = [('E','Emergency'), ('S', 'Standard')], validators=[DataRequired('请选择')])
	changeable = RadioField(label='Do you accept CHANGE?', choices = [('A','Accpet'), ('R', 'Refuse')], validators=[DataRequired('请选择')])
	description = StringField(label="Describe your pet's condition", validators=[DataRequired()])
	doctor = SelectField(label='希望预约哪位医生?', coerce=int, validators=[DataRequired()])
	submit = SubmitField('Comfirm and Submit')

    
class QuestionForm(FlaskForm):
    title = StringField('Question', validators=[DataRequired()])
    body = StringField('Question description')
    anonymity = BooleanField('anonymity')
    submit = SubmitField('Confirm')
    
class AnswerForm(FlaskForm):
    body = StringField('Answer', validators=[DataRequired()])
    submit = SubmitField('Reply')

class PetForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	age = IntegerField('Age', validators=[NumberRange(min=0,max=30)])
	category = RadioField(
        validators=[DataRequired('请选择宠物种类')],
        choices=[('dog', '狗'), ('cat', '猫')]
    )
	submit = SubmitField('Add')
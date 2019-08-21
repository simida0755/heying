# _*_ coding: utf-8 _*_
from wtforms import Form, StringField, RadioField, BooleanField
from wtforms.fields import core
from wtforms.validators import DataRequired, Length, Regexp, ValidationError

__author__ = 'john'

class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])


class UserForm(Form):
    name = StringField(
        '姓名', validators=[DataRequired(message='姓名不能为空'), Length(min=2, max=10,
                                                    message='姓名长度必须在2到10个字符之间')])
    gender = StringField('性别',validators=[DataRequired(message='性别不能为空')],)

    phone_number = StringField('手机号', validators=[DataRequired(message='手机号不能为空'),
                                            Regexp('^1[0-9]{10}$', 0, message='请输入正确的手机号')])
    district = StringField(
        '所在大区', validators=[DataRequired(message='所在大区不能为空'),
                            Length(min=2, max=10, message='没有找到这个大区')])

    subway_site = StringField(
        '附近的地铁站', validators=[DataRequired(message='所在地铁站大区不能为空'),
                            Length(min=2, max=10)])

    def validate_gender(self,field):
        if field.data not in ['男','女']:
            raise ValidationError("请在性别选项填写’男'或'女'")
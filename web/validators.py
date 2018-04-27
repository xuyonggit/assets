#-*-coding:utf-8-*-

import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

username_re = re.compile(r'^([a-zA-Z]{1}[\w]+?)$')
username = RegexValidator(username_re, u'用户名需由字母数字或下划线组成,首字母为字母', 'invalid')

password_re = re.compile(r'^.*$')
password = RegexValidator(password_re, u'密码最少为6位', 'invalid')
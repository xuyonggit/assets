# _*_ coding:utf-8 _*_

from django.forms.fields import Field, CharField
from .validators import username, password

class UsernameField(CharField):
    default_error_messages = {
        'invalid': u'用户名需由字母数字或下划线组成,首字母为字母',
        'required': u'用户名必须要填',
        'max_length': u'用户名至多为12位',
        'min_lenght': u'用户名至少为5位'
    }
    default_validators = [username]

    def clean(self, value):
        value = self.to_python(value).strip()
        return super(UsernameField, self).clean(value)

class PasswordField(CharField):
    default_error_messages = {
        'invalid': u'密码需由字母数字或下划线组成,首字母为字母',
        'required': u'密码必须要填',
        'max_length': u'密码至多为18位',
        'min_lenght': u'密码至少为8位'
    }
    default_validators = [password]
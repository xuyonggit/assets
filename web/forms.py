from django import forms
from .field import UsernameField, PasswordField
from django.contrib.auth import authenticate, login
from . import models


class In_repo(forms.Form):
    asset_id = forms.CharField(
        label='设备ID',
        widget=forms.TextInput(attrs={'class': 'form-control'}),

    )
    create_date = forms.DateField(
        label='归还日期',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    use_department = forms.ModelChoiceField(
        label='归还部门',
        empty_label='请选择部门',
        queryset=models.department.objects,
    )  # 使用部门
    use_people = forms.CharField(
        label='归还人',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )  # 使用人


class In_repo2(forms.Form):
    asset_id = forms.CharField(
        label='设备ID',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

class Out_repo(forms.Form):
    asset_id = forms.CharField(
        label='设备ID',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    create_date = forms.DateField(
        label='借用日期',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    use_department = forms.ModelChoiceField(
        label='借用部门',
        empty_label='请选择部门',
        queryset=models.department.objects,
    )  # 使用部门
    use_people = forms.CharField(
        label='借用人',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )  # 使用人


class LoginForm(forms.Form):
    username = UsernameField(required=True, max_length=12, min_length=5)
    password = PasswordField(required=True, max_length=18, min_length=8)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            # 如果成功返回对应的User对象，否则返回None(只是判断此用户是否存在，不判断是否is_active或者is_staff)
            if self.user_cache is None:
                raise forms.ValidationError(u'您输入的用户名或密码不正确!')
            elif not self.user_cache.is_active:
                raise forms.ValidationError(u'您输入的用户名或密码不正确!')
            else:
                login(self.request, self.user_cache)
            return self.cleaned_data

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class ChangePasswordForm(forms.Form):
    newpassword = PasswordField(required=True, max_length=12, min_length=5)
    renewpassword = PasswordField(required=True, max_length=12, min_length=6)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_password2(self):
        newpassword = self.cleaned_data.get('newpassword')
        renewpassword = self.cleaned_data.get('renewpassword')
        if newpassword and renewpassword:
            if newpassword != renewpassword:
                raise forms.ValidationError(u"此处必须输入和上栏密码相同的内容")
        raise forms.ValidationError(u"此处必须输入和上栏密码相同的内容")
        return renewpassword

    def save(self, commit=True):
        """
        Saves the new password.
        """
        self.user.set_password(self.cleaned_data["newpassword"])
        if commit:
            self.user.save()
        return self.user
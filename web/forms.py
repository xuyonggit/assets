from django import forms


class In_repo(forms.Form):
    asset_id = forms.CharField(
        label='设备ID',
        widget=forms.TextInput(attrs={'class': 'form-control'}),

    )
    create_date = forms.DateField(
        label='归还日期',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    use_department = forms.CharField(
        label='归还部门',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )  # 使用部门
    use_people = forms.CharField(
        label='归还人',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )  # 使用人


class Out_repo(forms.Form):
    asset_id = forms.CharField(
        label='设备ID',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    create_date = forms.DateField(
        label='借用日期',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    use_department = forms.CharField(
        label='借用部门',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )  # 使用部门
    use_people = forms.CharField(
        label='借用人',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )  # 使用人

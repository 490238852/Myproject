from django import forms
from django.core.exceptions import ValidationError
import re
from APP import models
def mobile_validate(values):
    mobile_re=re.compile(r'^(13[0-9]|15[0123456789]|17[39]|18[68])[0-9]{8}$')
    if not mobile_re.match(values):
        raise ValidationError('手机号码格式错误')

class UserRegister(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'用户名'}),
                               max_length=16,
                               error_messages={'required':'不能为空','max_length':'不能超过16个字'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required':"不能为空",'placeholder':'请输入密码'}),)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'请输入Email地址',}),
                             error_messages={'required':u'邮箱不能为空'})
    phone = forms.CharField(validators=[mobile_validate,],
                            error_messages={'required':'不能为空'},
                            widget=forms.TextInput(attrs={'class':'form-control','style':"color: red;",'placeholder':'请输入手机号'}),)
    content = forms.CharField(required=False,
                              widget=forms.Textarea(attrs={'cols':100,'placeholder':'请输入备注'}))
    country = (('1','China'),('2','USA'))
    countryChoice = forms.ChoiceField(choices=country)


    def clean_user(self):         #单个字段验证
        if self.cleaned_data.get('username') == "wangwu":
            self.add_error("username",'隔壁老王禁止注册')
        return self.cleaned_data.get("username")
    def clean(self):            #表单中所有数据的验证
        username_send = self.cleaned_data.get("username")
        password_send = self.cleaned_data.get("password")
        print('所有的data', self.cleaned_data)
        if username_send == password_send:
            raise ValidationError('账号密码不能相同')
    class Meta:
        fields= '__all__'


class AdminModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
        #fields = ('username', 'email')
        widgets = {
            'email': forms.PasswordInput(attrs={'class': "alex"}),
        }

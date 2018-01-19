from django import forms




class IndexForms(forms.Form):

    user_type_choice= (
        (0,u'普通用户'),
        (1,u'VIP用户'),
    )
    user_type = forms.IntegerField(
        widget=forms.widgets.Select(
            choices=user_type_choice,
            attrs={'class':'form-control'})
    )
    title = forms.CharField(max_length=20,
                            min_length=5,
                            error_messages={
                                'required':u'标题不能为空',
                                'min_length': u'标题最少为5个字符',
                                'max_length': u'标题最多为20个字符'
                            },
                            widget=forms.TextInput(
                                attrs={'class': "form-control",'placeholder': u'标题5-20个字符'}
                            )
                            )
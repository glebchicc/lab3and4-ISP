from django import forms
from django.contrib.auth.models import User


class CityChooseForm(forms.Form):
    CHOICES = (
        ('borisov', 'Борисов'),
        ('minsk', 'Минск'),
    )
    select = forms.ChoiceField(widget=forms.Select, choices=CHOICES, label="Город отправления")
    select2 = forms.ChoiceField(widget=forms.Select, choices=CHOICES, label="Город прибытия")


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

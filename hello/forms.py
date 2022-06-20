from django import forms
from django.contrib.auth.models import User

from hello.models import Bus


class CityChooseForm(forms.Form):
    CHOICES = (
        ('borisov', 'Борисов'),
        ('minsk', 'Минск'),
    )
    select = forms.ChoiceField(widget=forms.Select(attrs={'class': 'choice'}), choices=CHOICES,
                               label="Город отправления")
    select2 = forms.ChoiceField(widget=forms.Select(attrs={'class': 'choice'}), choices=CHOICES, label="Город прибытия")


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    password.widget.attrs.update({'class': 'myfield'})
    password2.widget.attrs.update({'class': 'myfield'})

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
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    username.widget.attrs.update({'class': 'myfield'})
    password.widget.attrs.update({'class': 'myfield'})


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = (
            'bus_number', 'departure_time', 'arrival_time', 'departure_place', 'arrival_place', 'place_cost', 'places',
            'size_of_bus')
        labels = {
            'departure_time': 'Время отправления (<дата> <время>)',
            'arrival_time': 'Время прибытия (<дата> <время>)',
        }

    def __init__(self, *args, **kwargs):
        super(BusForm,self).__init__(*args, **kwargs)
        self.fields['size_of_bus'].empty_label = 'Выберите'

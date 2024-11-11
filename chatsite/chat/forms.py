# Define os campos, tipos tamanhos e regras de formulários HTML

from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Email:',
        max_length=255,
        required=True
    )
    birth = forms.DateField(
        label='Nascimento:',
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    name = forms.CharField(
        label='Nome:',
        max_length=127,
        required=True
    )
    password = forms.CharField(
        label='Senha:',
        widget=forms.PasswordInput(),
        required=True
    )

# Django
from django import forms
# Models
from users.models import User, Profile

class ProfileForm(forms.Form):
    """Profile form"""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()

class ProfileSignup(forms.Form):
    """Profile form"""

    username = forms.CharField(min_length=4, max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, max_length=70, required=True)
    password_confirmation = forms.CharField(widget=forms.PasswordInput, max_length=70, required=True)
    first_name=forms.CharField(min_length=2, max_length=50)
    last_name=forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(widget=forms.EmailInput, max_length=150, required=True)

    def clean_username(self):
        """Validación si el usuario ya se encuentra en uso"""
        username = self.cleaned_data['username']
        username_token = User.objects.filter(username=username).exists()

        if username_token:
            raise forms.ValidationError('Usuario acualmente en uso')

        return username

    def clean(self):
        """Validación que las contraseñas sean iguales"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Contraseñas ingresadas no son iguales')

        return data

    def save(self):
        """Método para guardar un nuevo usuario"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import InsuredUser, Address

# CUSTOM REGISTRATION FORM
class RegistrationForm(UserCreationForm):
    """
    Custom user registration form.
    
    This form extends the UserCreationForm provided by Django.
    It includes additional fields such as first name, last name, email, phone number, street, house number, apartment number, city, and postal code.

    The 'password1' and 'password2' fields are used for password input and confirmation.

    Upon saving the form, it creates a new User instance along with associated InsuredUser and Address instances.
    """
    first_name = forms.CharField(label="Křestní jméno", max_length=100, required=True)
    last_name = forms.CharField(label="Příjmení", max_length=100, required=True)
    username = forms.CharField(label="Uživatelské jméno", max_length=150, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone_number = forms.CharField(label="Tel.č.", max_length=20, required=True)
    street = forms.CharField(label="Ulice", max_length=100, required=True)
    house_number = forms.IntegerField(label="Číslo popisné", required=True)
    apartment_number = forms.IntegerField(label="Číslo domu", required=False)
    city = forms.CharField(label="Město", max_length=100, required=True)
    post_code = forms.CharField(label="PSČ", max_length=20, required=True)
    password1 = forms.CharField(
        label="Heslo",
        strip=False,
        widget=forms.PasswordInput,
        help_text="Zadejte silné heslo."
    )
    password2 = forms.CharField(
        label="Heslo znovu",
        strip=False,
        widget=forms.PasswordInput,
        help_text="Zadejte heslo znovu pro kontrolu."
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'phone_number', 'street', 'house_number', 'apartment_number', 'city', 'post_code']


    def save(self, commit=True):
        """
        Save method overridden to create a new User instance and associated InsuredUser and Address instances upon form submission.
        """
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            insured_user = InsuredUser.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                phone_number=self.cleaned_data['phone_number']
            )

            address = Address.objects.create(
                user=user,
                street=self.cleaned_data['street'],
                house_number=self.cleaned_data['house_number'],
                apartment_number=self.cleaned_data['apartment_number'],
                city=self.cleaned_data['city'],
                post_code=self.cleaned_data['post_code']
            )

            insured_user.save()
            address.save()

        return user


# LOGIN FORM
class LoginForm(AuthenticationForm):
    """
    Form for user login.

    Inherits from AuthenticationForm provided by Django.

    Includes fields for username and password.
    """
    username = forms.CharField(label="Uživatelské jméno", max_length=150, required=True)
    password = forms.CharField(label="Heslo", strip=False, widget=forms.PasswordInput)


# USER UPDATE FORM
class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user information.

    Inherits from ModelForm provided by Django.

    Uses InsuredUser model and allows updating fields like first name, last name, email, and phone number.
    """
    class Meta:
        model = InsuredUser
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        labels = {
            'first_name': 'Křestní jméno',
            'last_name': 'Příjmení',
            'email': 'Email',
            'phone_number': 'Telefonní číslo',
        }

# ADDRESS UPDATE FORM
class AddressUpdateForm(forms.ModelForm):
    """
    Form for updating address information.

    Inherits from ModelForm provided by Django.

    Uses Address model and allows updating fields like street, house number, apartment number, city, and postal code.
    """
    class Meta:
        model = Address
        fields = ['street', 'house_number', 'apartment_number', 'city', 'post_code']
        labels = {
            'street': 'Ulice',
            'house_number': 'Číslo popisné',
            'apartment_number': 'Číslo domu',
            'city': 'Město',
            'post_code': 'PSČ',
        }

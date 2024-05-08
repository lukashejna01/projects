from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# INSURED USER
class InsuredUser(models.Model):
    """
    Model representing an insured user.

    Each insured user has a one-to-one relationship with a User instance, which is linked through the 'user' field.

    Attributes:
    - user: A OneToOneField representing the associated User instance.
    - first_name: A CharField storing the first name of the insured user.
    - last_name: A CharField storing the last name of the insured user.
    - email: An EmailField storing the email address of the insured user.
    - phone_number: A CharField storing the phone number of the insured user.

    Methods:
    - __str__: Returns a string representation of the insured user.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    phone_number = models.CharField(max_length=20, unique=True, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ADDRESS
class Address(models.Model):
    """
    Model representing an address associated with a user.

    Each address has a one-to-one relationship with a User instance, which is linked through the 'user' field.

    Attributes:
    - user: A OneToOneField representing the associated User instance.
    - street: A CharField storing the street name.
    - house_number: An IntegerField storing the house number.
    - apartment_number: An IntegerField storing the apartment number (optional, can be null).
    - city: A CharField storing the city name.
    - post_code: A CharField storing the postal code.

    Methods:
    - __str__: Returns a string representation of the address.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    street = models.CharField(max_length=100, blank=False)
    house_number = models.IntegerField(blank=False)
    apartment_number = models.IntegerField(null=True)
    city = models.CharField(max_length=100, blank=False)
    post_code = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f"{self.user.username}'s address"


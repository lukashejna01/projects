from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# TYPE OF INSURANCE
class TypeOfInsurance(models.Model):
    """
    Model representing the type of insurance.

    Attributes:
    - type: A CharField representing the type of insurance (e.g., "Health", "Life", "Car").

    Methods:
    - __str__: Returns a string representation of the type of insurance.
    """
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

# INSURANCE
class Insurance(models.Model):
    """
    Model representing an insurance policy.

    Attributes:
    - id: An AutoField serving as the primary key.
    - user: A ForeignKey representing the user associated with the insurance.
    - type: A ForeignKey representing the type of insurance.
    - amount: An IntegerField representing the amount of insurance coverage.
    - item: A CharField representing the item insured.
    - validity_from: A DateField representing the start date of validity.
    - validity_to: A DateField representing the end date of validity.

    Methods:
    - __str__: Returns a string representation of the insurance policy.
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeOfInsurance, null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False)
    item = models.CharField(max_length=50, blank=False)
    validity_from = models.DateField(blank=False)
    validity_to = models.DateField(blank=False)

    def __str__(self):
        return f"{self.user.username}'s insurance"
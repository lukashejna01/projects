from django import forms
from .models import TypeOfInsurance, Insurance

# INSURANCE CREATE FORM
class InsuranceForm(forms.ModelForm):
    """
    Form for creating a new insurance.

    Attributes:
    - type: A ModelChoiceField representing the type of insurance, populated with all available insurance types.
    - amount: An IntegerField for specifying the insurance amount.
    - item: A CharField for describing the insured item.
    - validity_from: A DateField for specifying the start date of insurance validity.
    - validity_to: A DateField for specifying the end date of insurance validity.

    Meta:
    - model: Specifies the Insurance model to which the form is linked.
    - fields: Specifies the fields to include in the form.

    Methods:
    - __init__: Customizes the form initialization to populate the 'type' field with all available insurance types.
    """
    type = forms.ModelChoiceField(queryset=TypeOfInsurance.objects.all(), label='Pojištění')
    amount = forms.IntegerField(label='Částka')
    item = forms.CharField(label='Předmět pojištění')
    validity_from = forms.DateField(label='Platnost od', widget=forms.DateInput(attrs={'type': 'date'}))
    validity_to = forms.DateField(label='Platnost do', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Insurance
        fields = ['type', 'amount', 'item', 'validity_from', 'validity_to']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].queryset = TypeOfInsurance.objects.all()


# INSURANCE UPDATE FORM
class InsuranceUpdateForm(forms.ModelForm):
    """
    Form for updating an existing insurance.

    Meta:
    - model: Specifies the Insurance model to which the form is linked.
    - fields: Specifies the fields to include in the form.
    - labels: Customizes field labels for the form.

    Methods:
    - __init__: Customizes the form initialization to populate the 'type' field with all available insurance types.
    """
    class Meta:
        model = Insurance
        fields = ['type', 'amount', 'item', 'validity_from', 'validity_to']
        labels = {'type': 'Pojištění', 'amount': 'Částka', 'item': 'Předmět pojištění', 'validity_from': 'Platnost od', 'validity_to': 'Platnost do'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].queryset = TypeOfInsurance.objects.all()

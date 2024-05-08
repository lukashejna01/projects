from django.shortcuts import render, redirect, get_object_or_404
from .forms import InsuranceForm, InsuranceUpdateForm
from django.urls import reverse
from .models import Insurance, TypeOfInsurance

# Create your views here.

# ADD INSURANCE
def add_insurance(request):
    """
    View for adding a new insurance.

    Args:
    - request: HTTP request object.

    Returns:
    - Rendered template with the insurance form.
    """
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            insurance = form.save(commit=False)
            insurance.user = request.user
            insurance.save()
            return redirect(reverse('profile', kwargs={'user_id': request.user.id}))
    else:
        form = InsuranceForm()
    return render(request, 'insurances/add_insurance.html', {'form': form})


# INSURANCE DETAIL
def insurance_view(request, insurance_id):
    """
    View for displaying details of a specific insurance.

    Args:
    - request: HTTP request object.
    - insurance_id: ID of the insurance to display.

    Returns:
    - Rendered template with insurance details.
    """
    insurance = Insurance.objects.get(id=insurance_id)
    return render(request, 'insurances/insurance_detail.html', {'insurance': insurance})


# UPDATE INSURANCE
def update_insurance(request, insurance_id):
    """
    View for updating an existing insurance.

    Args:
    - request: HTTP request object.
    - insurance_id: ID of the insurance to update.

    Returns:
    - Rendered template with the insurance update form.
    """
    insurance = Insurance.objects.get(id=insurance_id)
    if request.method == 'POST':
        form = InsuranceUpdateForm(request.POST, instance=insurance)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', kwargs={'user_id': request.user.id}))
    else:
        form = InsuranceUpdateForm(instance=insurance)
    
    return render(request, 'insurances/update_insurance.html', {'form': form})


# DELETE INSURANCE
def delete_insurance(request, insurance_id):
    """
    View for deleting an existing insurance.

    Args:
    - request: HTTP request object.
    - insurance_id: ID of the insurance to delete.

    Returns:
    - Rendered template for confirming deletion.
    """
    insurance = Insurance.objects.get(id=insurance_id)
    if request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            insurance.delete()
        return redirect(reverse('profile', kwargs={'user_id': request.user.id}))
    else:
        return render(request, 'insurances/delete_insurance.html')


# ALL TYPES OF INSURANCES
def all_insurance_types(request):
    """
    View for displaying all types of insurances.

    Args:
    - request: HTTP request object.

    Returns:
    - Rendered template with a list of insurance types.
    """
    types = TypeOfInsurance.objects.all()
    return render(request, 'insurances/insurance-types.html', {'types': types})

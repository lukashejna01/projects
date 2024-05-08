from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, UserUpdateForm, AddressUpdateForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from insurances.models import Insurance
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def home(request):
    """
    View for the home page displaying all insured users.

    Retrieves all non-staff users from the database.
    
    Args:
    - request: HTTP request object
    
    Returns:
    - Rendered response containing the 'insuredusers/index.html' template with the users data
    """
    users = User.objects.filter(is_staff=False).order_by('last_name')
    return render(request, 'insuredusers/index.html', {'users': users})

# REGISTER VIEW
def register_view(request):
    """
    View for user registration.

    Handles both GET and POST requests. 

    Args:
    - request: HTTP request object

    Returns:
    - Rendered response containing the registration form page with the form data
      or a redirect to the user's profile page upon successful registration
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            user_id = request.user.id
            return redirect('index')
    else:
        # The form remains empty if we visit the page for the first time.
        form = RegistrationForm()
    return render(request, 'insuredusers/register.html', {'form': form})

# LOGIN VIEW
def login_view(request):
    """
    View for user login.

    Handles both GET and POST requests.

    Args:
    - request: HTTP request object

    Returns:
    - Rendered response containing the login form page with the form data
      or a redirect to the user's profile page upon successful login
    """
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            user_id = request.user.id
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, "insuredusers/login.html", {'form': form})

# LOGOUT VIEW
def logout_view(request):
    """
    View for user logout.

    Handles POST request to log the user out and redirects them to the home page.

    Args:
    - request: HTTP request object

    Returns:
    - Redirects to the home page after successfully logging out the user
    """
    if request.method == 'POST':
        logout(request)
        return redirect('index')

# USER PROFILE VIEW
@login_required
def profile_view(request, user_id):
    """
    View for user profile page.

    Retrieves insured user details and insurances associated with the user based on the provided user_id.

    Args:
    - request: HTTP request object
    - user_id: ID of the user whose profile is being viewed

    Returns:
    - Renders the user profile page with user details, insured user details, address, and insurances
    """
    user = User.objects.get(id=user_id)
    insured_user = user.insureduser
    address = user.address
    insurances = Insurance.objects.filter(user=user)
    if not request.user.is_superuser and request.user != user:
        return HttpResponseForbidden("Nemáte oprávnění k zobrazení tohoto profilu.")
    return render(request, 'insuredusers/user_profile.html', {'user': user, 'insured_user': insured_user, 'address': address, 'insurances': insurances})

# USER UPDATE VIEW
@login_required
def update_view(request, user_id):
    """
    View for updating user profile.

    Handles form submission for updating user and address information.
    
    Args:
    - request: HTTP request object
    - user_id: ID of the user whose profile is being updated

    Returns:
    - Renders the update user profile page with user and address forms
    - Redirects to the user profile page upon successful update
    """
    user = User.objects.get(id=user_id)
    insured_user = user.insureduser
    address = user.address

    logged_user = request.user

    if not logged_user.is_superuser and logged_user != user:
        return HttpResponseForbidden("Nemáte oprávnění k zobrazení tohoto profilu.")
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=insured_user)
        address_form = AddressUpdateForm(request.POST, instance=address)
        if user_form.is_valid() and address_form.is_valid():
            user_form.save()
            address_form.save()
            return redirect(reverse('profile', kwargs={'user_id': user_id}))
    user_form = UserUpdateForm(instance=insured_user)
    address_form = AddressUpdateForm(instance=address)
    return render(request, 'insuredusers/update_user_profile.html', {'user_form': user_form, 'address_form': address_form})

# USER DELETE VIEW
@login_required
def delete_view(request, user_id):
    """
    View for deleting user profile.

    Retrieves user object based on the provided user_id.
    Handles form submission for confirming user deletion.
    
    Args:
    - request: HTTP request object
    - user_id: ID of the user whose profile is being deleted

    Returns:
    - Deletes the user profile upon confirmation and logs out the user, then redirects to the home page
    - Redirects to the user profile page if deletion is not confirmed
    - Renders the delete user profile page with confirmation form
    """
    user = User.objects.get(id=user_id)

    if not request.user.is_superuser and request.user != user:
        return HttpResponseForbidden("Nemáte oprávnění k zobrazení tohoto profilu.")
    
    if request.method == 'POST':
        if request.POST.get('delete') == 'yes':
            user.delete()
            logout(request)
            return redirect('index')
        return redirect(reverse('profile', kwargs={'user_id': user_id}))
    return render(request, 'insuredusers/delete_user_profile.html')


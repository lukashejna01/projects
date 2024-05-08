from django.shortcuts import render

# ABOUT APP
def about_app(request):
    """
    View for displaying the about page of the application.

    Args:
    - request: HTTP request object

    Returns:
    - Renders the about-app.html template
    """
    return render(request, 'about-app.html')
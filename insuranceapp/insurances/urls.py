from django.urls import path
from . import views

urlpatterns = [
    path('new-insurance/', views.add_insurance, name='new-insurance'),
    path('insurance-detail/<int:insurance_id>', views.insurance_view, name='insurance-detail'),
    path('edit-insurance/<int:insurance_id>', views.update_insurance, name='update-insurance'),
    path('delete-insurance/<int:insurance_id>', views.delete_insurance, name='delete-insurance'),
    path('all-types/', views.all_insurance_types, name='all-types'),
]
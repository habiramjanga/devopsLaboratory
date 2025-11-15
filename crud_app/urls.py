from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.get_patients, name='get_patients'),
    path('patients/create/', views.create_patient, name='create_patient'),
    path('patients/<int:id>/', views.patient_detail, name='patient_detail'),
]

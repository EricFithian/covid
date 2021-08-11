from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('testing/', views.TestListView.as_view(), name='testing'),
    path('testing/<int:id>/', views.testing_lookup, name='testing-detail'),
    path('testing/<int:id>/delete/', views.testing_delete, name='testing-delete'),
    path('vaccines/', views.VaccineListView.as_view(), name='vaccines'),
    path('vaccines/<int:id>/', views.vaccines_lookup, name='vaccine-detail'),
    path('vaccines/<int:id>/delete/', views.vaccines_delete, name='vaccine-delete'),
    path('vaccinations/', views.VaccinationsListView.as_view(), name='vaccinations'),
    path('vaccinations/<int:id>/', views.vaccinations_lookup, name='vaccinations-detail'),
    path('vaccinations/<int:id>/delete/', views.vaccinations_delete, name='vaccinations-delete'),
]

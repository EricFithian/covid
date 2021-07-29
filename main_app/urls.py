from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('testing/', views.TestListView.as_view(), name='testing'),
    path('testing/<int:id>/', views.testing_lookup, name='testing-detail'),
    path('testing/<int:id>/delete/', views.testing_delete, name='testing-delete'),
    path('vaccines/', views.vaccines, name='vaccines'),
]

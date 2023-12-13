from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.Show_form, name='show_form')
]

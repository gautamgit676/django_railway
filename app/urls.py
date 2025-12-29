from django.urls import path, include
from . import views
urlpatterns = [
    
    path('', views.School_data, name='schools'),
    path('school_f/', views.school_form, name='school_form'),
]
from django.conf.urls.i18n import set_language
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mazoon45/', views.mazoon45, name='mazoon45'),
    path('contact/', views.contact_view, name='contact'),  # Ensure this is unique
    path('mazoonlab/', views.mazoon_lab_view, name='mazoonlab'),  # Ensure this is unique
    path('i18n/setlang/', set_language, name='set_language'),
]

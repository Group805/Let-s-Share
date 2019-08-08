
from . import views
from django.urls import path


urlpatterns = [

    path(r'home/', views.index, name='home'),
    path(r'blogs/', views.blogs, name='blogs'),
    path(r'contact/', views.contact, name='contact'),
    path(r'login/', views.login, name='login'),
]



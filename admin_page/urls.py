from django.urls import path
from .views import UserRegisterView


urlpatterns = [
    
    path('Register',UserRegisterView.as_view(),name='register'),
    
    
]

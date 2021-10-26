from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('Profiles/', SignUpView.as_view(), name = 'signup'),
]
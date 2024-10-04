from django.urls import path
from .views import display_all_data

urlpatterns = [
    path('', display_all_data, name='home'),
]

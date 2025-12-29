from django.urls import path
from .views import simple_api2

urlpatterns = [
    path('simple/', simple_api2),
]

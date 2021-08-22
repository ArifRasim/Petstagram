from django.urls import path, include
from .views import landing_page

urlpatterns = [
    path('',landing_page)
]
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', core),
    path('details/', post_details),
]
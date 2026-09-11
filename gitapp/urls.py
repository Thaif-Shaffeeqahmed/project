from django.urls import path
from gitapp import views

urlpatterns = [
    path('show/',views.hello)
]
from django.urls import path
from . import views

app_name = 'users_area'

urlpatterns = [
    path('',views.Home.as_view(), name='home')
]


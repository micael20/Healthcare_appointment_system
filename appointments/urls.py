from django.urls import path  # type: ignore
from . import views

app_name = 'appointments'  # Define the namespace here

urlpatterns = [
    path('', views.index, name='index'),  # Default route
    path('index', views.index, name='index'),
    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('my_appointments/', views.my_appointments, name='my_appointments'),
]



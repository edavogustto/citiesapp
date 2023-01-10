from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('city/<int:id>', views.get_city, name='city')
]
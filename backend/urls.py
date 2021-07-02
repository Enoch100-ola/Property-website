from django.urls import path
from backend import views


app_name = 'backend'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('show-properties/', views.show_properties, name='show_properties'),
    path('add-property/', views.add_property, name='add_property'),
    path('add-location/', views.add_location, name='add_location'),
]

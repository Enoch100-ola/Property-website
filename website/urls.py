from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.about, name='about'),
    path('about-detail/<int:team_id>/', views.about_detail, name='about_detail'),
    path('agents/', views.agents, name='agents'),
    path('property-list/', views.property_list, name='property_list'),
    path('property-rent/', views.rent, name='rent'),
    path('property-buy/', views.buy, name='buy'),
    path('request/', views.request, name='request'),
    path('login-page/', views.login_view, name='login_view'),
    path('logout-page/', views.logout_view, name='logout_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register-page/', views.register, name='register'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('<slug:slug>/', views.property_detail, name='property_detail'),
]
    
   

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
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register-page/', views.register, name='register'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('logout-page/', views.logout_view, name='logout_view'),
#     path('add-location/', views.add_location, name='add_location'),
    path('add-property/', views.add_property, name='add_property'),
    path('view-properties/', views.view_properties_by_agent,
         name='view_properties_by_agent'),
    path('filter-data/', views.filter_data,
         name='filter_data'),
    path('edit-property/<int:prop_id>/', views.edit_property, name='edit_property'),
    path('delete-property/<int:prop_id>/',
         views.delete_property, name='delete_property'),
    path('<slug:slug>/', views.property_detail, name='property_detail'),
   
]
    
   

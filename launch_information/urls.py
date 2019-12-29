from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.upcoming,name='upcoming'),
    path('contacts', views.contacts,name='contacts'),
    path('launch_sites', views.launch_sites,name='launch_sites'),
    path('update_launch_sites_data', views.update_launch_sites_data,name='update_launch_sites_data'),
    path('pastlaunch', views.pastlaunch,name='pastlaunch'),
    path('update', views.update_launch_data,name='update_launch_data'),
    path('facts', views.facts,name='facts'),
    path('learn', views.learn,name='learn'),
    path('previous_launch', views.previous_launch, name='previous_launch'),
    path('past_launch', views.past_launch, name='past_launch'),

]
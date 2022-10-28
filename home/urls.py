from django.contrib import admin
from django.urls import path, include 
from home import views

# django admin customisation
admin.site.site_header="Developer Portal"
admin.site.site_title="Welcome to the Developer Portal"
admin.site.index_title="Developer Portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects')
]
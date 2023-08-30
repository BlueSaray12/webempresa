from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),
    path('contact/', views.store, name="contact"),
    path('blog/', views.store, name="blog"),
    path('sample/', views.store, name="sample"),
]

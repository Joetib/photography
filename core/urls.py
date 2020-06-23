from django.urls import path
from . import views 

app_name = 'core'


urlpatterns = [
    path('', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('services/', views.services, name="services"),
    path('pricing/', views.pricing, name="pricing"),
    path('appointment/create/<int:id>/', views.create_appointment, name="create-appointment"),
]
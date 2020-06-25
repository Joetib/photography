from django.urls import path
from . import views 

app_name = 'core'


urlpatterns = [
    path('', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('services/', views.services, name="services"),
    path('pricing/', views.pricing, name="pricing"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/profile/edit/', views.edit_profile, name="edit-profile"),
    path('appointment/create/<int:id>/', views.create_appointment, name="create-appointment"),
    path('appointment/details/<int:id>/', views.appointment_details, name="appointment-detail"),
    path('appointment/details/<int:id>/upload/ajax', views.ajax_file_upload, name="ajax-upload"),
    path('appointment/details/<int:id>/delete/', views.delete_appointment, name="delete-appointment"),
]
from django.contrib import admin
from .models import Category, Image, Service, DetailService
# Register your models here.


admin.site.register(Category)
admin.site.register(Service)
admin.site.register(DetailService)
admin.site.register(Image)
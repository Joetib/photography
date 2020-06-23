from django.contrib import admin
from .models import Category, Image, Service, DetailService, Slider, Appointment, PricingPlan, PricingFeature
# Register your models here.


admin.site.register(Category)
admin.site.register(Service)
admin.site.register(DetailService)
admin.site.register(Image)
admin.site.register(Slider)
admin.site.register(Appointment)
admin.site.register(PricingPlan)
admin.site.register(PricingFeature)

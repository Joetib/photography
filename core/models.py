from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username



class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")

class DetailService(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


class Category(models.Model):
    name = models.CharField(max_length=400)
    category_image = models.ImageField(upload_to="media/category/")



    def __str__(self):
        return self.name
    

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, related_name="images", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='media/images')
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)



class Slider(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=500)
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.title

class PricingFeature(models.Model):
    feature = models.CharField(max_length=100)

    def __str__(self):
        return self.feature

class PricingPlan(models.Model):
    title = models.CharField(max_length=100)
    price  = models.PositiveIntegerField()
    main_feature = models.CharField(max_length=50)
    features = models.ManyToManyField(PricingFeature, related_name='pricing_plans')
    
    def __str__(self):
        return f'{self.title} - GH₵ {self.price}'
    
    def get_pricing_plan_url(self):
        return reverse('core:create-appointment', kwargs={'id': self.id})

class Appointment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(PricingPlan, on_delete=models.CASCADE)
    venue = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Appointment on {self.date} by {self.user.username}'
    
    def get_absolute_url(self):
        return reverse('core:appointment-detail', kwargs={'id': self.id})


class AppointmentFile(models.Model):
    appointment = models.ForeignKey(Appointment, related_name="appointment_files", on_delete=models.CASCADE)
    file = models.FileField(upload_to="appointment/files")
    date_created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.file.name 

    def is_image(self):
        extensions = ('jpg', 'jpeg', 'png','PNG', 'jpe','jpf', 'gif')
        return self.file.name.split('.')[-1] in extensions
    def is_video(self):
        extensions = ('mp4', 'avi', 'mov')
        return self.file.name.split('.')[-1] in extensions



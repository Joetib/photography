from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


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





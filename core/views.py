from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from .models import Category, Image, Service, DetailService


def home(request):
    categories  = Category.objects.all()
    latest_images = Image.objects.all()[:11]
    services = Service.objects.all()
    return render(request, 'core/home.html', {'categories': categories, 'latest_images': latest_images, 'services': services})


def gallery(request):
    categories  = Category.objects.all()
    images = Image.objects.all()[:11]
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(images, per_page=10)
    if page_num < 1:
        page_num = 1
    if page_num >  paginator.num_pages:
        page_num = paginator.num_pages
    page = paginator.get_page(page_num)
    print(page, '\n\n')
    return render(request, 'core/gallery.html', {'categories': categories, 'images': page})


def services(request):
    services = Service.objects.all()
    detail_services  = DetailService.objects.all()
    return render(request, 'core/services.html', {'services': services, 'detail_services': detail_services})
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . import forms
# Create your views here.
from .models import Category, Image, Service, DetailService, Slider, PricingPlan


def home(request):
    categories  = Category.objects.all()
    latest_images = Image.objects.all()[:11]
    sliders = Slider.objects.all()
    services = Service.objects.all()
    return render(request, 'core/home.html', {'sliders': sliders, 'categories': categories, 'latest_images': latest_images, 'services': services})


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

def pricing(request):
    pricings = PricingPlan.objects.all()
    return render(request, "core/pricing.html", {'pricings': pricings})

def create_appointment(request, id):
    plan = get_object_or_404(PricingPlan, id=id)
    appointment_form = forms.CreateAppointmentForm(initial={'plan': plan})
    return render(request, 'core/create_appointment.html', {'plan': plan, 'appointment_form': appointment_form})

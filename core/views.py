from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from . import forms
from django.utils import timezone

# Create your views here.
from .models import (
    Category,
    Image,
    Service,
    DetailService,
    Slider,
    Appointment,
    PricingPlan,
    AppointmentFile,
)


def home(request):
    categories = Category.objects.all()
    latest_images = Image.objects.all()[:11]
    sliders = Slider.objects.all()
    services = Service.objects.all()
    return render(
        request,
        "core/home.html",
        {
            "sliders": sliders,
            "categories": categories,
            "latest_images": latest_images,
            "services": services,
        },
    )


def gallery(request):
    categories = Category.objects.all()
    images = Image.objects.all()[:11]
    page_num = int(request.GET.get("page", 1))
    paginator = Paginator(images, per_page=10)
    if page_num < 1:
        page_num = 1
    if page_num > paginator.num_pages:
        page_num = paginator.num_pages
    page = paginator.get_page(page_num)
    print(page, "\n\n")
    return render(
        request, "core/gallery.html", {"categories": categories, "images": page}
    )


def services(request):
    services = Service.objects.all()
    detail_services = DetailService.objects.all()
    return render(
        request,
        "core/services.html",
        {"services": services, "detail_services": detail_services},
    )


def pricing(request):
    pricings = PricingPlan.objects.all()
    return render(request, "core/pricing.html", {"pricings": pricings})


def create_appointment(request, id):
    plan = get_object_or_404(PricingPlan, id=id)
    if request.method == "POST":
        appointment_form = forms.CreateAppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('core:dashboard')
        else:
            print(request.POST.get("date"))
            print("\n\nform is invalid", appointment_form.errors, "\n\n")

    else:
        appointment_form = forms.CreateAppointmentForm(initial={"plan": plan})
    return render(
        request,
        "core/create_appointment.html",
        {"plan": plan, "appointment_form": appointment_form},
    )

@login_required
def dashboard(request):
    user = request.user
    pending_appointments = Appointment.objects.filter(user=request.user, completed=False)
    completed_appointments = Appointment.objects.filter(user=request.user, completed=True)
    profile_form = forms.ProfileForm(instance=request.user.profile)
    return render(
        request,
        "core/dashboard.html",
        {
            'profile_form': profile_form,
            "user": user,
            "pending_appointments": pending_appointments,
            "completed_appointments": completed_appointments,
            "total_appointments": len(pending_appointments)+len(completed_appointments),
        },
    )

@login_required
def appointment_details(request, id):
    appointment = get_object_or_404(Appointment, id=id, user=request.user)
    profile_form = forms.ProfileForm(instance=request.user.profile)
    return render(request, 'core/appointment_details.html', {'profile_form': profile_form,'appointment': appointment})

@login_required
def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id, user=request.user)
    if request.GET.get('confirmed'):
        appointment.delete()
        return redirect('core:dashboard')
    profile_form = forms.ProfileForm(instance=request.user.profile)
    return render(request, 'core/appointment_delete.html', {'profile_form': profile_form,'appointment': appointment})

@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = forms.ProfileForm(request.POST, files=request.FILES,instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
    return redirect('core:dashboard')


def ajax_file_upload(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    
    form  = forms.AppointmentImageUpload(request.POST, files=request.FILES)
    files  = request.FILES.getlist('files')
    if form.is_valid():
        print(files)
        for f in files:
            try:
                appointment_image = AppointmentFile.objects.create(appointment=appointment, file=f)
                appointment_image.save()
            except Exception as e:
                print(e)
        appointment.completed = True
        appointment.save()
    return JsonResponse({'success': True})
from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by(
        '-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    search_fields = Car.objects.values(
        'brand', 'model', 'city', 'body_style', 'year')
    # model_search = Car.objects.values_list('model', flat=True).distinct()  # To fetch unique value

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'search_fields': search_fields
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')

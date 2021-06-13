from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')

def about_detail(request):
    return render(request, 'website/about-detail.html')

def agents(request):
    return render(request, 'website/agent.html')


def property_list(request):
    return render(request, 'website/view-list.html')

def property_detail(request):
    return render(request, 'website/property-details.html')


def rent(request):
    return render(request, 'website/rent.html')


def buy(request):
    return render(request, 'website/buy.html')


def request(request):
    return render(request, 'website/request.html')


def login_view(request):
    return render(request, 'website/login.html')



def confirm_logout(request):
    return render(request, 'website/confirm-logout.html')


def dashboard(request):
    return render(request, 'website/dashboard.html')


def register(request):
    return render(request, 'website/register.html')


def add_location(request):
    return render(request, 'website/add-location.html')


def add_property(request):
    return render(request, 'website/add-property.html')







from django.shortcuts import render
from website.models import *
from backend.forms import *
from website.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def dashboard(request):
    all_prop = Property.objects.count()
    rent = Property.objects.filter(offer_type='Rent').count()
    sale = Property.objects.filter(offer_type='Sale').count()
    duplex = Property.objects.filter(property_type_id__name='Duplex').count()
    context = {
        'rent':rent,
        'sale': sale,
        'duplex': duplex,
        'all_prop': all_prop,
    }

    return render(request, 'backend/index.html', context)


@login_required(login_url='/pages/login-page/')
def show_properties(request):
    show = Property.objects.order_by('-created')
    return render(request, 'backend/view-properties.html', {'show': show})


@login_required(login_url='/pages/login-page/')
def add_location(request):
    if request.method == 'POST':
        location_form = AddLocation(request.POST)
        if location_form.is_valid():
            location_form.save()
            messages.success(request, 'Location Added Successfully')
    else:
        location_form = AddLocation()
    return render(request, 'backend/add-loc.html', {'loc': location_form})


def add_property(request):
    if request.method == 'POST':
        property_form = AdminPropertyForm(request.POST, request.FILES)
        if property_form.is_valid():
            property_form.save()
            messages.success(request, 'Property added')
    else:
        property_form = AdminPropertyForm()
    return render(request, 'backend/add-property.html', {'property': property_form})

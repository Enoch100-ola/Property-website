from django.shortcuts import render
from website.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.

def home(request):
    rent = Property.objects.filter(offer_type='Rent').order_by('-created')[:3]
    sale = Property.objects.filter(offer_type='Sale').order_by('-created')[:3]
    context = {
        'rent_key':rent,
        'sale_key':sale
    }
    return render(request, 'website/index.html', context)


def about(request):
    team = Team.objects.order_by('-created')
    return render(request, 'website/about.html', {'members':team})

def about_detail(request, team_id):
    team_detail = Team.objects.get(id=team_id)
    return render(request, 'website/about-detail.html', {'team':team_detail})

def agents(request):
    return render(request, 'website/agent.html')


def property_list(request):
    return render(request, 'website/view-list.html')

def property_detail(request, slug):
    try:

        prop = Property.objects.get(slug=slug)
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            print(name, email, phone)
            prop = Property.objects.get(slug=slug)
            agent = prop.agent_id
            location = prop.location_id
            agent_email = prop.agent_id.email
            subject = 'Contact Agent Form'
            context = {
                'name':name,
                'email':email,
                'phone':phone,
                'agent':agent,
                'location':location
            }
            html_message = render_to_string('website/mail-template.html', context)
            plain_message = strip_tags(html_message)
            from_email = settings.FROM_EMAIL
            send = mail.send_mail(subject, plain_message, from_email, [
                           agent_email,], html_message=html_message)
            if send:
                ContactAgent.objects.create(name=name, email=email, phone=phone, agent_id=agent, location_id=location)
                messages.success(request, 'Message Sent')
                print("Success")
            else:
                messages.error(request, 'Email not sent')
        return render(request, 'website/property-details.html', {'single_prop': prop})
    except ObjectDoesNotExist as error:
        print(f'You have this error {error}')
        return render(request, 'website/404.html')
    


def rent(request):
    rent = Property.objects.filter(offer_type='Rent').order_by('-created')
    return render(request, 'website/rent.html', {'rent_key':rent})


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







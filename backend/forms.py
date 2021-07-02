from django import forms
from website.models import *
from django.core import validators


class AddLocation(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Add Location'
        })
    )
    catch_bot = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        validators=[validators.MaxLengthValidator(0), ]
    )

    class Meta():
        model = Location
        fields = '__all__'

    def clean_name(self):
        loc_name = self.cleaned_data.get('name').capitalize()
        if Location.objects.filter(name=loc_name).exists():
            raise forms.ValidationError(f'{loc_name} already exist')
        return loc_name


class AdminPropertyForm(forms.ModelForm):
	RENT = 'Rent'
	SALE = 'Sale'
	CHOOSE = ''
	OFFER_TYPE = [
	    (RENT, 'Rent'),
	    (SALE, 'Sale'),
	    (CHOOSE, 'Choose An Offer Type'),
	]
	property_name = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Property Name'}
        ))
	slug = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Put a hyphen for your slug name'}
        ))
	property_img1 = forms.ImageField(widget=forms.ClearableFileInput())
	property_img2 = forms.ImageField(widget=forms.ClearableFileInput())
	property_img3 = forms.ImageField(widget=forms.ClearableFileInput())
	prize = forms.DecimalField(widget=forms.NumberInput(
            attrs={'class': 'form-control', }
        ))
	property_address = forms.CharField(widget=forms.Textarea(
            attrs={'class': 'form-control'}
        ))
	property_description = forms.CharField(widget=forms.Textarea(
            attrs={'class': 'form-control'}
        ))
	rooms = forms.IntegerField(required=False, widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        ))
	offer_type = forms.CharField(widget=forms.Select(attrs={'class': 'form-control', }, choices=OFFER_TYPE),
                              )
	location_id = forms.ModelChoiceField(
            label='Location',
            queryset=Location.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            empty_label='Select Location'
        )
	agent_id = forms.ModelChoiceField(
            label='Agents',
            queryset=User.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            empty_label='Select Location'
        )
        
	property_type_id = forms.ModelChoiceField(
            label='Property Type',
            queryset=PropertyType.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            empty_label='Select Property Type'
        )
	approve = forms.BooleanField(required=False, widget=forms.CheckboxInput())
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput(
	), validators=[validators.MaxLengthValidator(0), ])

	class Meta():
		model = Property
		exclude = ('created', 'modified', 'approve')
        # fields = ('approve', 'property_type_id', 'property_name')




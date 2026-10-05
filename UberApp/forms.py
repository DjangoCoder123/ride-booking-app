from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Pickup Address'}))
    destination = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Destination'}))
    phone_num = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
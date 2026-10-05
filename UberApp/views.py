from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from UberApp.forms import BookingForm
from UberApp.models import RideBooking


class Index(TemplateView):
     template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Fees(TemplateView):
    template_name = 'fees.html'


def Book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            data = form.cleaned_data

            # 1. READ THE BUTTON: Capture which button was clicked
            clicked_button = request.POST.get('booking_action')
            is_vip_status = True if clicked_button == 'vip' else False

            # 2. ASSIGN USER: Grab the logged-in user account if signed in
            current_user = request.user if request.user.is_authenticated else None

            # 3. SAVE TO DATABASE: Create the record with the VIP status and User
            RideBooking.objects.create(
                user=current_user,
                name=data['name'],
                address=data['address'],
                destination=data['destination'],
                phone_num=data['phone_num'],
                email=data['email'],
                is_vip=is_vip_status  # <-- This passes True or False to the database
            )

            # 4. EMAIL CONTENT: Include the VIP status in your notification email
            status_text = "✨ YES (Premium VIP Member)" if is_vip_status else "No (Standard Booking)"
            subject = f"New Ride Booking from {data['name']}"
            message = f"""
            You have received a new ride booking request:

            Account Username: {current_user.username if current_user else 'Guest (Not Logged In)'}
            Name: {data['name']}
            VIP Member: {status_text}
            Phone: {data['phone_num']}
            Email: {data['email']}
            Pickup Address: {data['address']}
            Destination: {data['destination']}
            """

            from_email = None  # Inherits config from settings.py
            recipient_list = ['basophil2025@outlook.com']

            # Send the email
            send_mail(subject, message, from_email, recipient_list)

            # 5. MESSAGES & REDIRECT: Alert banners based on choice
            if is_vip_status:
                messages.success(request, "🎉 Your booking request has been sent! Welcome to the VIP list!")
            else:
                messages.success(request, "Your booking request has been sent successfully!")

            return redirect('/book/')
    else:
        form = BookingForm()

    return render(request, 'bookings.html', {'form': form})

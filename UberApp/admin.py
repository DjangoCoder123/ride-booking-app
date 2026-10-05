# UberApp/admin.py
from django.contrib import admin
from .models import RideBooking

@admin.register(RideBooking)
class RideBookingAdmin(admin.ModelAdmin):
    # Added 'user' to the list display columns
    list_display = ('user', 'name', 'is_vip', 'phone_num', 'email', 'created_at')
    list_filter = ('is_vip', 'created_at')
    search_fields = ('user__username', 'name', 'email') # Allows searching by username too

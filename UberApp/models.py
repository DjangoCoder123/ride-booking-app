# UberApp/models.py
from django.db import models
from django.contrib.auth.models import User  # <-- Import the User model


class RideBooking(models.Model):
    # 👇 Links this booking to a specific user account.
    # If the user account is deleted, their bookings are deleted too (CASCADE).
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings', null=True, blank=True)

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=20)
    email = models.EmailField()
    is_vip = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "VIP" if self.is_vip else "Standard"
        # Shows their logged-in username alongside the text name
        username = self.user.username if self.user else "Guest"
        return f"{username} account: {self.name} ({status})"

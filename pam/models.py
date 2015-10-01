from django.db import models

# Create your models here.


class Device(models.Model):
    mac_address = models.CharField(max_length=12, default="000000000000", help_text="Device MAC address")
    description = models.TextField(default="", help_text="Host")
    last_seen = models.DateTimeField(help_text="Date last seen")
    show_in_overview = models.BooleanField(default=True, help_text="Show in animation?")
    currently_in_space = models.BooleanField(default=False, help_text="Currently in the space?")


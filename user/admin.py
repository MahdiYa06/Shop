from django.contrib import admin
from .models import profile, Address, User



admin.site.register(User)
admin.site.register(profile)
admin.site.register(Address)
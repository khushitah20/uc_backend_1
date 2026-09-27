from django.contrib import admin
from .models import Club, Member, Membership

# Register your models here.
admin.site.register(Club)
admin.site.register(Member)
admin.site.register(Membership)
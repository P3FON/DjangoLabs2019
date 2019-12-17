from django.contrib import admin
from .models import Audiobook, Review

# Register your models here.
admin.site.register(Audiobook)
admin.site.register(Review)
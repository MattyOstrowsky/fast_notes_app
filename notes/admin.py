from django.contrib import admin

# Register your models here.
from .models import Note, UserAccount


admin.site.register(Note)
admin.site.register(UserAccount)

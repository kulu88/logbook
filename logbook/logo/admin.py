from django.contrib import admin

# Register your models here.
from .models import(Aircraft, People, Airport, Flight)

admin.site.register(Aircraft)
admin.site.register(People)
admin.site.register(Airport)
admin.site.register(Flight)
# admin.site.register(Hour)
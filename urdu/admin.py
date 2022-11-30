from django.contrib import admin

# Register your models here.
from .models import School
admin.site.register(School)

from .models import madarsa
admin.site.register(madarsa)

from .models import contact
admin.site.register(contact)

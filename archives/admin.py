from django.contrib import admin
from archives.models import Animal


# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Animal, AnimalAdmin)

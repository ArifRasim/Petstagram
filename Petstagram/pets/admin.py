from django.contrib import admin

# Register your models here.
from Petstagram.pets.models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ['name','type','age','likes_count']
    list_filter = ['name']

    def likes_count(self,obj):
        return obj.like_set.count()

admin.site.register(Pet,PetAdmin)


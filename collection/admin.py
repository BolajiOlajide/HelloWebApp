from django.contrib import admin

from collection.models import Resources

# set up automated slug creation
class ResourceAdmin(admin.ModelAdmin):
    model = Resources
    list_display = ('name', 'description', 'url',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Resources, ResourceAdmin)

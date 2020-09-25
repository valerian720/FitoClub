from django.contrib import admin
from .models import *

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0
    min_num = 1

class EmailInline(admin.TabularInline):
    model = Email
    extra = 0
    min_num = 1

class FlatProducerAdmin(admin.ModelAdmin):
    inlines = [
        PhoneInline,EmailInline,
    ]

# https://stackoverflow.com/questions/2431727/django-admin-hide-a-model
class DisabledModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'content', 'sites')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name'),
        }),
    )
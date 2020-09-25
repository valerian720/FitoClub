from django.contrib import admin

from .models import *
from .admin_display_templates import *


admin.site.register(Producer, FlatProducerAdmin)
admin.site.register(ProductType)
admin.site.register(Phone, DisabledModelAdmin)
admin.site.register(Email, DisabledModelAdmin)
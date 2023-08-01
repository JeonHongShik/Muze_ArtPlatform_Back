from django.contrib import admin
from .models import ConsumUser

# Register your models here.
class ConsumesAdmin(admin.ModelAdmin):
    list_display = ('Age','Education','Career','Award','Introduce','Created','Updated')
    
admin.site.register(ConsumUser,ConsumesAdmin)
from django.contrib import admin
from .models import Trainer
# Register your models here.

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active','joined_at')
    list_display_links=('id','name')
    list_filter=('name',)
    list_editable=('is_active',)
    search_fields = ('name',)
    list_per_page=25


admin.site.register(Trainer,TrainerAdmin)
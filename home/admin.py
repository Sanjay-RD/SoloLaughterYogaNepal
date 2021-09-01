from django.contrib import admin
from .models import Trainer, Schedule, Intro, Advantage
# Register your models here.

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active','joined_at')
    list_display_links=('id','name')
    list_filter=('name',)
    list_editable=('is_active',)
    search_fields = ('name',)
    list_per_page=25


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','title','trainer','date')
    list_display_links = ('title',)
    list_filter=('title',)
    search_fields=('title','trainer')
    list_per_page=25


class IntroAdmin(admin.ModelAdmin):
    list_display=('id','title','description','is_display')
    list_display_links=('title',)
    list_editable = ('is_display',)
    search_fields = ('title',)
    list_per_page = 20


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','is_display')
    list_display_links = ('title',)
    list_editable = ('is_display',)
    search_fields = ('title',)
    list_per_page = 25


admin.site.register(Trainer,TrainerAdmin)
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Intro,IntroAdmin)
admin.site.register(Advantage,AdvantageAdmin)
from django.contrib import admin

# Register your models here.
from .models import Diary


class DiaryAdmin(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(Diary, DiaryAdmin)

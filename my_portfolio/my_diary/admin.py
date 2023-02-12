from django.contrib import admin
from rangefilter.filter import DateRangeFilter

# Register your models here.
from .models import Diary


class DiaryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = (("created_at", DateRangeFilter), ("updated_at", DateRangeFilter))


admin.site.register(Diary, DiaryAdmin)

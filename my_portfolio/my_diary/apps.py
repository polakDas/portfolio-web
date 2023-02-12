from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MyDiaryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "my_portfolio.my_diary"
    verbose_name = _("My Diaries")

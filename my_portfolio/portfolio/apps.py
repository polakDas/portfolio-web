# flake8: noqa
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "my_portfolio.portfolio"
    verbose_name = _("My Portfolio")

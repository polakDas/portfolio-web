from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from my_portfolio.my_diary.api.views import DiaryViewSet
from my_portfolio.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("diary", DiaryViewSet)


app_name = "api"
urlpatterns = router.urls

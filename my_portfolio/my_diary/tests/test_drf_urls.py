from django.urls import resolve, reverse

from my_portfolio.my_diary.models import Diary


def test_diary_detail(diary: Diary):
    assert (
        reverse("api:diary-detail", kwargs={"pk": diary.pk})
        == f"/api/users/{diary.pk}/"
    )
    assert resolve(f"/api/diaries/{diary.pk}/").view_name == "api:diary-detail"


def test_diary_list():
    assert reverse("api:diary-list") == "/api/diaries/"
    assert resolve("/api/diaries/").view_name == "api:diary-list"

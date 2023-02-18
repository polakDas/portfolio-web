from django.db import models
from django.urls import reverse


# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Written at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def get_absolute_url(self):
        """Get the diary detail view.

        Returns:
            str: URL for diary detail.
        """
        return reverse("my_diary:detail", kwargs={"pk": str(self.pk)})

    class Meta:
        verbose_name = "My Diary"
        verbose_name_plural = "My Diaries"

    def __str__(self):
        return self.title

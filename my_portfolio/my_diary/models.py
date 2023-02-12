from django.db import models


# Create your models here.
class Diary(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "My Diary"
        verbose_name_plural = "My Diaries"

    def __str__(self):
        return self.title

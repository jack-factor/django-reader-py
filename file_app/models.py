from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.urls import reverse


class History(models.Model):
    title = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='document')
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('history', kwargs={})

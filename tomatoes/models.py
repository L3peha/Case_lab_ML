from django.conf import settings
from django.db import models



class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    film = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField()
    status = models.BooleanField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
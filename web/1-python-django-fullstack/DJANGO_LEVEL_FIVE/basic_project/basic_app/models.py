from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='pictures', blank=True)

    def __str__(self):
        """Represent this model in string."""
        return self.user.username

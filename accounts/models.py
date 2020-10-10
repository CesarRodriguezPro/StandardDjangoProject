from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # necesssairz juste ppur la redefinir
    username = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(default=15)
    # date_of_birth = models.DateField(null=True, blank=True)
    consent_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.username

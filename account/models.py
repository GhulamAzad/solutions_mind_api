from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


USER_TYPE_CHOICES = (
    ('student', 'Student'),
    ('professional', 'Professional'),
    ('other', 'Other')
)


class User(AbstractUser):
    """
    This mode will be used to store all user related information.
    """
    user_type = models.CharField(max_length=12,
                                 choices=USER_TYPE_CHOICES,
                                 default='other')
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return "{}".format(self.username)

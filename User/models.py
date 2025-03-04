from django.db import models
from django.contrib.auth.models import AbstractUser
from User.managers import UserManager

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField('Email Address',
                          unique=True
                          )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'

    name = models.CharField(max_length =30)
    surname = models.CharField(max_length =30)
    birth_date = models.DateField()
    phone = models.CharField(max_length=13)
    image = models.ImageField(upload_to='media/')
    XP = models.IntegerField(default=0)
    gender = models.CharField(choices=GenderChoices.choices, max_length =30, default=GenderChoices.MALE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def xp_calculation(self):
        a = self.XP * 9
        return a

    def level_calculation(self):
        pass

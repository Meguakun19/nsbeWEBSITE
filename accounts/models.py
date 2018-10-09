from django.db import models

# Create your models here.
#Blueprint for how you want to store your data
#Make a class in here and automatically what django is going to do is
# its going to get each variable from those classes and convert it to a column in our database.

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    #add additional fields in here

    def __str__(self):
        return "@{}".format(self.username)

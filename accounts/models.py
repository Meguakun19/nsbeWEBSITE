# Create your models here.
#Blueprint for how you want to store your data
#Make a class in here and automatically what django is going to do is
# its going to get each variable from those classes and convert it to a column in our database.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    #add additional fields in here
    username = models.CharField(verbose_name='Name',max_length=45, unique=True)
    email_address = models.EmailField(verbose_name='Email Address', max_length=255, unique=True, null=True, blank=True)
    phone_number = models.CharField(verbose_name='Phone Number',max_length=11, null=True, blank=True)
    date_joined_nsbe = models.CharField(verbose_name='Date Joined NSBE?',max_length=25, null=True)
    dues_paid = models.BooleanField(verbose_name='Dues Paid?',default=False)
    eboard_member = models.BooleanField(verbose_name='E-Board Member?',default=False)

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    CLASSIFICATION_CHOICES =(
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('FR', 'Senior'),
    )
    classification = models.CharField(
        max_length=2,
        choices = CLASSIFICATION_CHOICES,
        default=FRESHMAN,
    )


    def __str__(self):
        return "@{}".format(self.username)

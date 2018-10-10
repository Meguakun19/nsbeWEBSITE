# Generated by Django 2.0.5 on 2018-10-10 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_grade_point_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email_address',
            field=models.EmailField(max_length=255, null=True, unique=True, verbose_name='Email Address'),
        ),
    ]

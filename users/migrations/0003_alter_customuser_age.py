# Generated by Django 4.1.6 on 2023-02-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
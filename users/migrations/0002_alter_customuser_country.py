# Generated by Django 4.1.6 on 2023-02-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.TextField(default='', max_length=255),
        ),
    ]
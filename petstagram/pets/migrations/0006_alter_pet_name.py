# Generated by Django 3.2.3 on 2021-08-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotto',
            name='number',
            field=models.IntegerField(),
        ),
    ]
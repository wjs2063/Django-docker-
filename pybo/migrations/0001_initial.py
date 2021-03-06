# Generated by Django 3.2.13 on 2022-06-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('number', models.IntegerField(default=1000, help_text='천원에서 20만원까지 입력하세요', verbose_name=' 금액을 입력하세요 ')),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]

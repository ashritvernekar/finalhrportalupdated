# Generated by Django 4.0.4 on 2022-05-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basicinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('qualifications', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=100)),
                ('ctc', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='cid',
            field=models.AutoField(),
            
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='contact',
            field=models.IntegerField(),
        ),
    ]

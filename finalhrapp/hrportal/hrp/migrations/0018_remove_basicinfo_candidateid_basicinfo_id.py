# Generated by Django 4.0.4 on 2022-06-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0017_delete_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basicinfo',
            name='candidateid',
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='id',
            field=models.BigAutoField(),
            
        ),
    ]

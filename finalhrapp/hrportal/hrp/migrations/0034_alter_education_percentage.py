# Generated by Django 4.0.4 on 2022-07-02 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0033_alter_basicinfo_exp_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]

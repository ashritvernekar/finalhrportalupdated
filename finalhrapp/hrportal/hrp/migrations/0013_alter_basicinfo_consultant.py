# Generated by Django 4.0.4 on 2022-06-15 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0012_alter_basicinfo_consultant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='consultant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consultant', to='hrp.consultanttable'),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-23 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0028_rename_info_consultant_hr_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicinfo',
            name='applied_for',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='call_or_interview_remarks',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='current_job_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='current_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='date_of_joining',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='designated_as',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='exp_ctc',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='exp_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='interview_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='interviewed_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='interviewed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='notice_period',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='permanent_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='present_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='ready_to_relocate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='resume_received_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='resume_received_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='total_experience',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('basic_skills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basic_skills', to='hrp.basicinfo')),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-11 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progrews'), ('done', 'Done')], default='new', max_length=100),
        ),
    ]

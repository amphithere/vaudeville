# Generated by Django 2.0.6 on 2018-06-11 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-23 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_auto_20200323_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='username',
            new_name='name',
        ),
    ]

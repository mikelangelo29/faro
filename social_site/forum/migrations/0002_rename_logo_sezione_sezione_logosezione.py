# Generated by Django 4.2.1 on 2023-06-10 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sezione',
            old_name='logo_sezione',
            new_name='logosezione',
        ),
    ]

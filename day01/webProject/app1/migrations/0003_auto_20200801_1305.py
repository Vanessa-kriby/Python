# Generated by Django 3.0.8 on 2020-08-01 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200801_0451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='cname',
            new_name='Cname',
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-08 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='gno',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]

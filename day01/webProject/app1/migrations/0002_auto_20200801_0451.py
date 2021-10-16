# Generated by Django 3.0.8 on 2020-08-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('Ccode', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='scourses',
            field=models.ManyToManyField(to='app1.Courses'),
        ),
    ]

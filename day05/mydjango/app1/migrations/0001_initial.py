# Generated by Django 3.0.8 on 2020-08-15 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('gain_date', models.DateField()),
            ],
            options={
                'db_table': 'consequence',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=50)),
                ('tgender', models.CharField(max_length=20)),
                ('jobtitle', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='TeachPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.FloatField()),
                ('teach_date', models.DateField()),
                ('evaluation_method', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Department')),
            ],
            options={
                'db_table': 'teachplan',
            },
        ),
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textbook', models.CharField(max_length=50)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Teacher')),
            ],
            options={
                'db_table': 'teaching',
            },
        ),
        migrations.AddField(
            model_name='teacher',
            name='teachCourse',
            field=models.ManyToManyField(through='app1.Teaching', to='app1.Course'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=50)),
                ('sgender', models.CharField(max_length=20)),
                ('studentCourse', models.ManyToManyField(through='app1.Consequence', to='app1.Course')),
                ('studentDepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Department')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='departmentCourses',
            field=models.ManyToManyField(through='app1.TeachPlan', to='app1.Department'),
        ),
        migrations.AddField(
            model_name='consequence',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Student'),
        ),
        migrations.AddField(
            model_name='consequence',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Course'),
        ),
    ]

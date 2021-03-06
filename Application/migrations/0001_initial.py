# Generated by Django 3.0.3 on 2020-03-23 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('building', models.CharField(max_length=200)),
                ('budget', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('tot_cred', models.IntegerField()),
                ('stud_img', models.ImageField(upload_to='media/')),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('credits', models.IntegerField()),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application.Department')),
            ],
        ),
    ]

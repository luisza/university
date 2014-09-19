# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('credits', models.IntegerField(default=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('budget', models.FloatField()),
                ('start_date', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hire_date', models.DateField(auto_now_add=True)),
                ('departament', models.ForeignKey(to='university.Departament')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enrollment_date', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(height_field=531, width_field=413, upload_to=b'students')),
                ('user', models.OneToOneField(related_name=b'student_of', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='instructor',
            name='office',
            field=models.ForeignKey(to='university.Office'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(related_name=b'instructor_of', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(to='university.Instructor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='university.Student'),
            preserve_default=True,
        ),
    ]

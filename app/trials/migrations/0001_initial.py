# Generated by Django 3.1.2 on 2022-05-15 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdentificationModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NCTId', models.CharField(max_length=30, null=True)),
                ('BriefTitle', models.CharField(max_length=300, null=True)),
                ('OfficialTitle', models.CharField(max_length=600, null=True)),
                ('Acronym', models.CharField(max_length=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]

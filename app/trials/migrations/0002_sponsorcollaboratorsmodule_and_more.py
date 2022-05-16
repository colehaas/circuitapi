# Generated by Django 4.0.4 on 2022-05-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorCollaboratorsModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='statusmodule',
            name='CompletionDate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='statusmodule',
            name='OverallStatus',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='statusmodule',
            name='PrimaryCompletionDate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='statusmodule',
            name='StartDate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='statusmodule',
            name='StatusVerifiedDate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='statusmodule',
            name='WhyStopped',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

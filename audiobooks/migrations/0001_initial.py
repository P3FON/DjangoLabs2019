# Generated by Django 2.1.4 on 2019-12-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(blank=True, max_length=150)),
                ('narrator', models.CharField(blank=True, max_length=150)),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='date of release')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars'), (0, 'undecided')], default=0)),
                ('comment', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
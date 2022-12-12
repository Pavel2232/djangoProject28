# Generated by Django 4.1.4 on 2022-12-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=100)),
                ('is_published', models.BooleanField()),
            ],
        ),
    ]

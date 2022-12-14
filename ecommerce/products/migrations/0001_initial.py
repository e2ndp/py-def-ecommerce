# Generated by Django 4.1 on 2022-08-08 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]

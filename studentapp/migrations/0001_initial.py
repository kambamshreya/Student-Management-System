# Generated by Django 4.0.5 on 2022-06-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('roll_no', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
            ],
        ),
    ]
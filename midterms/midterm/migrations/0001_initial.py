# Generated by Django 5.1.5 on 2025-03-10 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('assigned_personnel', models.CharField(max_length=255)),
                ('due_date', models.DateField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Blog', '0002_delete_flower'),
    ]

    operations = [
        migrations.CreateModel(
            name='karbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('name_flower', models.CharField(blank=True, max_length=100)),
                ('number', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]

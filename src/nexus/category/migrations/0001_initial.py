# Generated by Django 5.0.1 on 2024-02-05 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('icon', models.CharField(max_length=20)),
                ('main_icon', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('sorting', models.SmallIntegerField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
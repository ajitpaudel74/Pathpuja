# Generated by Django 4.2.5 on 2024-09-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_pandit_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='pandit',
            name='contact',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

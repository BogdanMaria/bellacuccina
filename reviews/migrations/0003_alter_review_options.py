# Generated by Django 3.2.25 on 2024-06-27 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_time_posted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-time_posted']},
        ),
    ]

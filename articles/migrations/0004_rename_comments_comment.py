# Generated by Django 4.2.4 on 2023-08-19 21:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("articles", "0003_comments"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Comments",
            new_name="Comment",
        ),
    ]

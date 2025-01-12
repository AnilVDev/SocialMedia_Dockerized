# Generated by Django 4.2.11 on 2024-05-14 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0008_notification_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="like_or_comment_user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications_liked_or_commented",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications_received",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

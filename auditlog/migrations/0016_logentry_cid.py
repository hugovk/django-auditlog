# Generated by Django 4.1.4 on 2022-12-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auditlog", "0015_alter_logentry_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="logentry",
            name="cid",
            field=models.CharField(
                blank=True,
                db_index=True,
                max_length=255,
                null=True,
                verbose_name="Correlation ID",
            ),
        ),
    ]

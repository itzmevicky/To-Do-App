# Generated by Django 4.1.3 on 2022-12-23 18:15

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("Task", "0002_alter_todotask_duedate_alter_todotask_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todotask",
            name="Tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]

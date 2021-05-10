# Generated by Django 3.0.6 on 2021-02-23 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_pointsgained"),
    ]

    operations = [
        migrations.AddField(
            model_name="pointsgained",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="backend.PostComment",
            ),
        ),
    ]
# Generated by Django 3.0.5 on 2020-07-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_auto_20200630_2240"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment", options={"ordering": ("-creation_date",)},
        ),
        migrations.AlterField(
            model_name="comment",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-12-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pdfExtractor", "0002_pdf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pdf",
            name="file",
            field=models.FileField(
                default=None, max_length=250, null=True, upload_to="pdf/"
            ),
        ),
    ]

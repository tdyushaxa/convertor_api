# Generated by Django 5.0.3 on 2024-04-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_pdf_to_word_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf_to_word',
            name='result',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_pdf_to_word_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf_to_word',
            name='word_file',
            field=models.FileField(blank=True, null=True, upload_to='word'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_ocr'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageOCR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Image-ocr')),
                ('lang', models.CharField(blank=True, max_length=200, null=True)),
                ('file_name', models.CharField(blank=True, max_length=200, null=True)),
                ('result', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='OCR',
        ),
    ]
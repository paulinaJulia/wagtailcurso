# Generated by Django 3.2.10 on 2022-01-20 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogdetailpage_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogdetailpage',
            old_name='blog_image',
            new_name='banner_image',
        ),
    ]
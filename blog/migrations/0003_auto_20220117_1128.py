# Generated by Django 3.2.10 on 2022-01-17 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0002_blogauthos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogAuthos',
            new_name='BlogAuthor',
        ),
        migrations.AlterModelOptions(
            name='blogauthor',
            options={'verbose_name': 'Blog Author', 'verbose_name_plural': 'Blog Authors'},
        ),
    ]

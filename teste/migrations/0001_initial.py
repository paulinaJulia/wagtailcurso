# Generated by Django 3.2.10 on 2022-02-16 19:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('titulo', models.CharField(blank=True, max_length=200, verbose_name='Titulo da Página')),
                ('subtitle', models.CharField(blank=True, max_length=200, verbose_name='Subtítulo da Página')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Página mark',
                'verbose_name_plural': 'Páginas Mark',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MarketFragmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('texto', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titulo')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='E-mail')),
                ('website', models.URLField(blank=True, null=True, verbose_name='site')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Url ')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Icone')),
                ('locale', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Proveedor - Market Assets',
                'verbose_name_plural': 'Proveedores - Market Assets',
                'unique_together': {('translation_key', 'locale')},
            },
        ),
    ]

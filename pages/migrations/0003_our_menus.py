# Generated by Django 4.2.6 on 2023-12-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_mainscrollmodel_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our_Menus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_menus', models.ImageField(upload_to='main-menus')),
                ('title_menus', models.CharField(max_length=50)),
                ('info_menus', models.CharField(max_length=255)),
                ('money', models.CharField(max_length=100)),
            ],
        ),
    ]

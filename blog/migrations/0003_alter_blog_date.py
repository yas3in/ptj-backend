# Generated by Django 4.2 on 2024-11-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_created='1403/08/16'),
        ),
    ]

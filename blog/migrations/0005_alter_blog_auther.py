# Generated by Django 4.2 on 2024-11-08 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_user_username_user_full_name_alter_user_email'),
        ('blog', '0004_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuul_name', to='main.user'),
        ),
    ]
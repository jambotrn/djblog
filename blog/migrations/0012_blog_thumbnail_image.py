# Generated by Django 4.0.3 on 2022-08-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_options_remove_blog_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_pictures'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='articles.tag'),
        ),
    ]

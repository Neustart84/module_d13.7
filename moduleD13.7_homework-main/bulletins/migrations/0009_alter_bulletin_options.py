# Generated by Django 4.2.1 on 2023-06-09 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0008_alter_bulletin_bul_text_alter_news_news_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bulletin',
            options={'ordering': ['-create_time']},
        ),
    ]

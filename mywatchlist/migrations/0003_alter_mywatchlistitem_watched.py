# Generated by Django 4.1 on 2022-11-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_alter_mywatchlistitem_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlistitem',
            name='watched',
            field=models.BooleanField(default=False),
        ),
    ]

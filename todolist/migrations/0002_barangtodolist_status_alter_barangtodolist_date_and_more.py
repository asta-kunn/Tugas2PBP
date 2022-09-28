# Generated by Django 4.1 on 2022-09-25 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barangtodolist',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='barangtodolist',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='barangtodolist',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='barangtodolist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

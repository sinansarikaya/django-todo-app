# Generated by Django 4.2.1 on 2023-05-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todosmodel',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]

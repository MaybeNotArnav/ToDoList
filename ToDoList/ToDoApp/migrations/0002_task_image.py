# Generated by Django 4.1.1 on 2022-10-21 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

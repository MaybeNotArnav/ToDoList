# Generated by Django 4.1.1 on 2022-10-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0002_task_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(null=True, upload_to='test/'),
        ),
    ]
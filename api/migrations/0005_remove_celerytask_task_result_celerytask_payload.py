# Generated by Django 4.0.3 on 2022-03-24 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_celerytask_task_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celerytask',
            name='task_result',
        ),
        migrations.AddField(
            model_name='celerytask',
            name='payload',
            field=models.TextField(blank=True, null=True),
        ),
    ]
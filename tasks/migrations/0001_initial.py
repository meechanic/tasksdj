# Generated by Django 3.0 on 2023-07-09 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('human_description', models.TextField(blank=True)),
                ('machine_description', models.TextField(blank=True)),
                ('supercategory', models.TextField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('subcategory', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name', 'human_description'],
            },
        ),
        migrations.CreateModel(
            name='TaskTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
                ('value', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasktag_task', to='tasks.Task')),
            ],
            options={
                'ordering': ['key', 'value'],
                'unique_together': {('key', 'value', 'task')},
            },
        ),
    ]

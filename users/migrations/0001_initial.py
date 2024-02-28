# Generated by Django 4.2.10 on 2024-02-28 06:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentId', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('JobID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200, unique=True)),
                ('DepartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.department')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('UserID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=300)),
                ('JobID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.job')),
            ],
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='work_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_w', models.DateField(max_length=10)),
                ('time_w', models.TimeField(max_length=10)),
                ('work_w', models.CharField(max_length=30)),
                ('fio_w', models.CharField(max_length=20)),
                ('tel_w', models.CharField(max_length=20)),
                ('comlete_w', models.BooleanField(default=False)),
                ('created_w', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
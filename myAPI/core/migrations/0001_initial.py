# Generated by Django 4.1.7 on 2023-03-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('father_name', models.CharField(max_length=100)),
            ],
        ),
    ]

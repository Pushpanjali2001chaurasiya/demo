# Generated by Django 4.2.4 on 2023-08-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Age', models.CharField(max_length=2)),
                ('Mobile', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=50)),
                ('Trade', models.CharField(max_length=10)),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
    ]
# Generated by Django 3.2.10 on 2022-04-17 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cartlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=200, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
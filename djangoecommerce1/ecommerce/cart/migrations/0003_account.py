# Generated by Django 4.2.1 on 2023-07-10 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acctype', models.CharField(max_length=20)),
                ('accno', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]

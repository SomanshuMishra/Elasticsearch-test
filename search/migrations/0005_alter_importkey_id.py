# Generated by Django 4.0.3 on 2022-03-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_n'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importkey',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

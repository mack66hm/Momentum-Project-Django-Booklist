# Generated by Django 3.0.3 on 2020-02-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200228_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]

# Generated by Django 2.1.7 on 2019-05-12 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190512_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='strike_price',
            field=models.CharField(max_length=40),
        ),
    ]
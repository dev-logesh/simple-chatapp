# Generated by Django 3.0.14 on 2022-07-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0011_auto_20220713_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='room',
            name='blockuser',
            field=models.TextField(blank=True),
        ),
    ]

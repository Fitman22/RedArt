# Generated by Django 5.0.7 on 2024-07-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seguidor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguidor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

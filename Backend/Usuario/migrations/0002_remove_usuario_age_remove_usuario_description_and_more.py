# Generated by Django 5.0.7 on 2024-07-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='age',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='description',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telephone',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
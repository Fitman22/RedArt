from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=models.CASCADE, related_name='usuarioSeguido', to='Usuario.Usuario')),
            ],
        ),
    ]

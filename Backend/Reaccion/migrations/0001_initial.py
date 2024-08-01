from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # Asegúrate de que los modelos Ilustracion y Usuario están listados aquí
        ('Ilustracion', '0001_initial'),  # Reemplaza con el nombre correcto del archivo de migración inicial de Ilustracion
        ('Usuario', '0001_initial'),      # Reemplaza con el nombre correcto del archivo de migración inicial de Usuario
    ]

    operations = [
        migrations.CreateModel(
            name='Reaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.CharField(max_length=50)),
                ('love', models.CharField(max_length=50)),
                ('funny', models.CharField(max_length=50)),
                ('sad', models.CharField(max_length=50)),
                ('ilustracion', models.ForeignKey(on_delete=models.CASCADE, related_name='ilustracionReaccion', to='Ilustracion.Ilustracion')),
                ('usuario', models.ForeignKey(on_delete=models.CASCADE, related_name='usuarioReaccion', to='Usuario.Usuario')),
            ],
        ),
    ]

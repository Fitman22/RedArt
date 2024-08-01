from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ilustracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lasName', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField()),
                ('password', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('telephone', models.IntegerField()),
                ('ilustracion', models.ForeignKey(on_delete=models.CASCADE, related_name='ilustracionUsuario', to='Ilustracion.Ilustracion')),
            ],
        ),
    ]

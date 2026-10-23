
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proyecto',
            new_name='Project',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='fecha_creacion',
            new_name='created_at',
        ),
        migrations.RenameModel(
            old_name='Tarea',
            new_name='Task',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='titulo',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='proyecto',
            new_name='project',
        ),
    ]


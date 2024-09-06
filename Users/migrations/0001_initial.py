# Generated by Django 4.2.11 on 2024-04-21 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rols',
            fields=[
                ('Id_Rol', models.AutoField(primary_key=True, serialize=False)),
                ('Rol_name', models.CharField(choices=[('Customer', 'Customer'), ('Delivery', 'Delivery')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('Id_user', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=25)),
                ('Id_Rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.rols')),
            ],
        ),
    ]

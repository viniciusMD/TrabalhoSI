# Generated by Django 3.0.5 on 2020-04-24 22:12

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField(default=0)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='funcionario',
            managers=[
            ],
        ),
    ]
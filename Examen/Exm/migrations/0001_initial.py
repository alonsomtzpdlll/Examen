# Generated by Django 3.0.5 on 2020-04-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Altura', models.CharField(max_length=100)),
                ('Peso', models.CharField(max_length=100)),
                ('Velocidad', models.CharField(max_length=100)),
                ('Color', models.CharField(max_length=100)),
            ],
        ),
    ]

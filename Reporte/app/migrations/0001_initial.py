# Generated by Django 3.2.12 on 2023-04-14 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parasito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('departamento', models.CharField(max_length=30)),
                ('prevalencia', models.IntegerField()),
            ],
        ),
    ]

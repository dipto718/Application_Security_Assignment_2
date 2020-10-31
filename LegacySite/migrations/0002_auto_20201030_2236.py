# Generated by Django 3.1.2 on 2020-10-30 22:36

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('LegacySite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='amount',
            field=django_cryptography.fields.encrypt(models.IntegerField()),
        ),
        migrations.AlterField(
            model_name='card',
            name='data',
            field=django_cryptography.fields.encrypt(models.BinaryField(unique=True)),
        ),
        migrations.AlterField(
            model_name='card',
            name='fp',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=100, unique=True)),
        ),
        migrations.AlterField(
            model_name='card',
            name='used',
            field=django_cryptography.fields.encrypt(models.BooleanField(default=False)),
        ),
    ]

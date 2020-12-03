# Generated by Django 2.2.2 on 2020-10-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 't_basic_unit',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('phone', models.CharField(blank=True, max_length=60)),
                ('email', models.CharField(blank=True, max_length=60)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 't_supplier',
            },
        ),
    ]
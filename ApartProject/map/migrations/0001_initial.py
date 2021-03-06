# Generated by Django 4.0.3 on 2022-06-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addrdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('dong', models.CharField(blank=True, max_length=50, null=True)),
                ('apt', models.CharField(blank=True, max_length=50, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('bunji', models.CharField(blank=True, max_length=50, null=True)),
                ('addr', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'addrData',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('gu', models.CharField(blank=True, max_length=45, null=True)),
                ('dong', models.CharField(blank=True, max_length=45, null=True)),
                ('apart', models.CharField(blank=True, max_length=45, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('we', models.CharField(blank=True, max_length=45, null=True)),
                ('gd', models.CharField(blank=True, max_length=45, null=True)),
                ('juso', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
    ]

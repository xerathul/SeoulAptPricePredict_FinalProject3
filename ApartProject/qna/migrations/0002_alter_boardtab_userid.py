# Generated by Django 4.0.3 on 2022-06-13 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardtab',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users.users'),
        ),
    ]

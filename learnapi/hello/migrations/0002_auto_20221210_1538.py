# Generated by Django 3.2.5 on 2022-12-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]

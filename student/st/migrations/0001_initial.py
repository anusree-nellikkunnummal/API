# Generated by Django 4.0.5 on 2022-12-08 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20, unique=True)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phonenumber', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('log_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='st.log')),
            ],
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_height', models.FloatField()),
                ('max_height', models.FloatField()),
                ('min_width', models.FloatField()),
                ('max_width', models.FloatField()),
                ('min_size', models.FloatField()),
                ('max_size', models.FloatField()),
                ('is_jpg', models.BooleanField()),
                ('is_png', models.BooleanField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]

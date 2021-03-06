# Generated by Django 2.2.1 on 2019-07-31 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
    ]

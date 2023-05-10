# Generated by Django 4.1.7 on 2023-04-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=250)),
                ('Picture', models.ImageField(upload_to='pics')),
                ('Details', models.TextField()),
            ],
        ),
    ]

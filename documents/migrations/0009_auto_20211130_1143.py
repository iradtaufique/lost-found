# Generated by Django 3.2.9 on 2021-11-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0008_idcollection_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idcollection',
            name='name',
        ),
        migrations.AddField(
            model_name='idcollection',
            name='first_name',
            field=models.CharField(default='First_name', max_length=225),
        ),
        migrations.AddField(
            model_name='idcollection',
            name='second_name',
            field=models.CharField(default='second_name', max_length=225),
        ),
    ]

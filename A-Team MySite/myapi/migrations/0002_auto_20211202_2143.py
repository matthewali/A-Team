# Generated by Django 2.2.12 on 2021-12-02 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['LName', 'FName']},
        ),
    ]

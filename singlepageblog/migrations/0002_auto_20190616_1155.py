# Generated by Django 2.2 on 2019-06-16 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('singlepageblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date'], 'verbose_name': 'My Stories'},
        ),
    ]

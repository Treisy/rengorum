# Generated by Django 2.0.3 on 2018-04-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]

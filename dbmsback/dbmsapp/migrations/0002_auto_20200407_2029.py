# Generated by Django 3.0.4 on 2020-04-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

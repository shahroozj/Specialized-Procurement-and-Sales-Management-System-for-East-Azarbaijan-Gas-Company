# Generated by Django 2.2.4 on 2019-08-18 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resid', '0005_auto_20190804_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resid',
            name='shomare',
            field=models.CharField(max_length=500, null=True, verbose_name='شماره رسید'),
        ),
    ]
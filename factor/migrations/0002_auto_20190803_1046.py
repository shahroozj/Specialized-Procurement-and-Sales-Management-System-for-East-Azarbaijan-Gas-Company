# Generated by Django 2.2.4 on 2019-08-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factor',
            name='shomare',
            field=models.CharField(max_length=100, null=True, verbose_name='شماره فاکتور'),
        ),
    ]
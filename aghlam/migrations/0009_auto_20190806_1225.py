# Generated by Django 2.2.4 on 2019-08-06 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aghlam', '0008_auto_20190806_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aghlam',
            name='meghdar',
            field=models.IntegerField(blank=True, null=True, verbose_name='مقدار'),
        ),
        migrations.AlterField(
            model_name='aghlam',
            name='taghaza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='taghaza', to='taghaza.Taghaza', verbose_name='تقاضا'),
        ),
    ]
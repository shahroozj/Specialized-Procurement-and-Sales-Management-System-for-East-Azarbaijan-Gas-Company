# Generated by Django 2.2.2 on 2019-07-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taghaza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taghaza',
            name='vahed',
            field=models.IntegerField(choices=[(1, 'بهره\u200cبرداری'), (2, 'امور رفاهی'), (3, 'اندازه\u200cگیری و توزیع گاز'), (4, 'حراست'), (5, 'خدمات طرح\u200cها'), (6, 'گازرسانی صنایع')], max_length=200, null=True, verbose_name='واحد'),
        ),
    ]
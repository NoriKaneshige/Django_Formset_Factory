# Generated by Django 3.0.6 on 2020-05-06 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('1', 'female'), ('2', 'male')], max_length=1, verbose_name='sex'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(verbose_name='weight'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='yearly_income',
            field=models.IntegerField(verbose_name='salary(K)'),
        ),
    ]
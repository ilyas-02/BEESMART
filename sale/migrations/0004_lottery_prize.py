# Generated by Django 3.2 on 2022-11-30 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_auto_20221129_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('start_date', models.DateTimeField(verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(verbose_name='Дата окончания')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картирнка')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lotteries', to='sale.shop', verbose_name='Магаазин')),
            ],
            options={
                'verbose_name': 'Лоторея',
                'verbose_name_plural': 'Лотореи',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картирнка')),
                ('lottery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prizes', to='sale.lottery', verbose_name='Лоторея')),
            ],
            options={
                'verbose_name': 'Приз',
                'verbose_name_plural': 'Призы',
            },
        ),
    ]
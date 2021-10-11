# Generated by Django 3.1 on 2021-05-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revenue_name', models.CharField(max_length=50)),
                ('revenue_amount', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Revenue ',
                'verbose_name_plural': 'Revenues',
            },
        ),
        migrations.CreateModel(
            name='Taxrate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_rate', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Taxrate ',
                'verbose_name_plural': 'Taxrate',
            },
        ),
    ]

# Generated by Django 3.1 on 2021-05-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomestatement', '0006_taxrate_active_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxrate',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

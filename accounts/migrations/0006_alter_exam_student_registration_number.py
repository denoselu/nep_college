# Generated by Django 3.2.4 on 2021-07-29 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_enrollmentfee_reg_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='student_registration_number',
            field=models.CharField(max_length=50),
        ),
    ]

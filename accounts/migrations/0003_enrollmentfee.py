# Generated by Django 3.2 on 2021-06-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_from', models.CharField(max_length=150)),
                ('Registration_admission_fee', models.IntegerField(default=0)),
                ('Tution_fee', models.IntegerField(default=0)),
                ('boarding_hostel_fees', models.IntegerField(default=0)),
                ('repair_and_maintanance', models.IntegerField(default=0)),
                ('electricity_water_and_conservancy', models.IntegerField(default=0)),
                ('activity_fund', models.IntegerField(default=0)),
                ('medical_fud_insurance', models.IntegerField(default=0)),
                ('rent_hire', models.IntegerField(default=0)),
                ('examination', models.IntegerField(default=0)),
                ('computer_studies', models.IntegerField(default=0)),
                ('production_contracts', models.IntegerField(default=0)),
                ('evening_classes', models.IntegerField(default=0)),
                ('citc_uniform_badge_id_card_t_shirt', models.IntegerField(default=0)),
                ('sundry_debtors_fees_arrears', models.IntegerField(default=0)),
                ('income_genarating_act', models.IntegerField(default=0)),
                ('miscellaneous', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Enrollment Fee',
                'verbose_name_plural': 'Enrollment Fees ',
            },
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_lowpriority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lowpriority',
            old_name='No Of Beneficiary',
            new_name='NoOfBeneficiary',
        ),
        migrations.RenameField(
            model_name='lowpriority',
            old_name='Release Amount',
            new_name='ReleasedAmount',
        ),
        migrations.RenameField(
            model_name='lowpriority',
            old_name='Sanction Amount',
            new_name='SanctionAmount',
        ),
        migrations.AlterField(
            model_name='lowpriority',
            name='SpentAmount',
            field=models.CharField(max_length=120, verbose_name='SpentAmount'),
        ),
    ]

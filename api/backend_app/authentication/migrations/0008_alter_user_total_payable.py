# Generated by Django 4.0 on 2021-12-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_emi_loanee_id_alter_user_total_payable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='total_payable',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='total_payable'),
        ),
    ]
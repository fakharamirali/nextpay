# Generated by Django 4.2.5 on 2023-09-20 13:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0001_initial"),
    ]
    
    operations = [
        migrations.AlterModelOptions(
            name="payportal",
            options={
                "permissions": [("secret", "Access secret data of pay portal")],
                "verbose_name": "Pay Portal",
                "verbose_name_plural": "Pay Portals",
            },
        ),
        migrations.AlterModelOptions(
            name="transaction",
            options={
                "default_permissions": [
                    ("create", "Can Create a new Transaction"),
                    ("verify", "Can verify a transaction with check"),
                    ("force_pay", "Can set it paid without check"),
                    ("delete_finished", "Delete finished transactions"),
                    ("delete_force_all", "Delete transactions"),
                ],
                "verbose_name": "Transaction",
                "verbose_name_plural": "Transactions",
            },
        ),
        migrations.AlterField(
            model_name="payportal",
            name="backend",
            field=models.CharField(
                choices=[
                    ("payment.payment_backends.nextpay.NextpayBackend", "Nextpay")
                ],
                max_length=512,
                verbose_name="Backend",
            ),
        ),
        migrations.AlterField(
            model_name="payportal",
            name="default_currency",
            field=models.CharField(
                blank=True,
                choices=[(None, "Not set Default"), ("IRR", "Rial"), ("IRT", "Toman")],
                max_length=10,
                null=True,
                validators=[django.core.validators.RegexValidator("^\\w+$")],
                verbose_name="Default Currency",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="currency",
            field=models.CharField(
                choices=[(None, "Not set Default"), ("IRR", "Rial"), ("IRT", "Toman")],
                max_length=10,
                validators=[django.core.validators.RegexValidator("^\\w$")],
                verbose_name="Currency",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="status",
            field=models.SmallIntegerField(
                choices=[
                    (-3, "Refund failed by lake of funds"),
                    (-2, "Refund Failed"),
                    (-1, "Refunded"),
                    (0, "Successful"),
                    (1, "Wait ..."),
                    (2, "Canceled"),
                    (3, "Wait for Bank"),
                    (4, "Canceled By User"),
                    (5, "Failed"),
                    (6, "Api Key is invalid"),
                ],
                verbose_name="Status",
            ),
        ),
    ]
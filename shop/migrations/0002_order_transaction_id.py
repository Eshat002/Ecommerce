# Generated by Django 3.2.18 on 2023-05-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alumni_alumni_no_alumni_is_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='is_paid',
        ),
        migrations.AddField(
            model_name='alumni',
            name='razor_order_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='alumni',
            name='razor_payment_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='alumni_no',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

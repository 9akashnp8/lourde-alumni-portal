# Generated by Django 4.0.4 on 2022-06-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_alumni_is_paid_alumni_razor_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='is_paid',
            field=models.BooleanField(blank=True, default=True),
            preserve_default=False,
        ),
    ]

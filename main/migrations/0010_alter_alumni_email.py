# Generated by Django 4.0.4 on 2022-06-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_alumni_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

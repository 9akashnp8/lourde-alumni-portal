# Generated by Django 4.0.4 on 2022-06-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_alumni_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
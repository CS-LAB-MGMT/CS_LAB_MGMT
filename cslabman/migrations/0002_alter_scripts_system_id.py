# Generated by Django 3.2.7 on 2021-10-07 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cslabman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scripts',
            name='system_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cslabman.systems'),
        ),
    ]

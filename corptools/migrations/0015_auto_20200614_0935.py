# Generated by Django 2.2.12 on 2020-06-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0014_characteraudit_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skilltotals',
            name='unallocated_sp',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
# Generated by Django 4.0.2 on 2022-05-16 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0073_remove_miningtaxpaymentcorp_corp_delete_miningtax_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evelocation',
            name='managed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evelocation',
            name='managed_char',
            field=models.ForeignKey(blank=True, default=None, null=True,
                                    on_delete=django.db.models.deletion.CASCADE, to='corptools.characteraudit'),
        ),
        migrations.AddField(
            model_name='evelocation',
            name='managed_corp',
            field=models.ForeignKey(blank=True, default=None, null=True,
                                    on_delete=django.db.models.deletion.CASCADE, to='corptools.corporationaudit'),
        ),
    ]
# Generated by Django 3.0.3 on 2020-02-15 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='password',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]

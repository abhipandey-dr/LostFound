# Generated by Django 3.0.3 on 2021-04-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210418_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdata',
            name='Description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
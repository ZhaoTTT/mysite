# Generated by Django 2.1.15 on 2021-11-17 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdaweb', '0002_auto_20211118_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcfrecommendation',
            name='imageURL',
            field=models.CharField(max_length=200),
        ),
    ]

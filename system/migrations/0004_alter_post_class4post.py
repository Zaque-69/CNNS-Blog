# Generated by Django 4.2.4 on 2023-10-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_postx_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='class4post',
            field=models.CharField(max_length=30),
        ),
    ]

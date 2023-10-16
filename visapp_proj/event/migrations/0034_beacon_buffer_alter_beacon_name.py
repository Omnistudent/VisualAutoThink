# Generated by Django 4.2 on 2023-04-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0033_userprofile_temp_question_area_holder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='buffer',
            field=models.IntegerField(default=0, verbose_name='buffer'),
        ),
        migrations.AlterField(
            model_name='beacon',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Beacon Name'),
        ),
    ]

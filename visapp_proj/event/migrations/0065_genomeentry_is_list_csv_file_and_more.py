# Generated by Django 4.2.4 on 2023-10-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0064_genomeentry_button_analyse_results_isok'),
    ]

    operations = [
        migrations.AddField(
            model_name='genomeentry',
            name='is_list_csv_file',
            field=models.CharField(default='', max_length=120, verbose_name='is_list_csv_file'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_list_csv_file_dir',
            field=models.CharField(default='D:/is_csvs/', max_length=120, verbose_name='is_list_csv_file_dir'),
        ),
    ]

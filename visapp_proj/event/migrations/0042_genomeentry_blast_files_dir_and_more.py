# Generated by Django 4.2.4 on 2023-10-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0041_genomeentry_genome_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='genomeentry',
            name='blast_files_dir',
            field=models.CharField(default='D:/blastresults/', max_length=120, verbose_name='blast_files_dir'),
        ),
        migrations.AlterField(
            model_name='genomeentry',
            name='files_num',
            field=models.IntegerField(default=-1, verbose_name='files_num'),
        ),
    ]

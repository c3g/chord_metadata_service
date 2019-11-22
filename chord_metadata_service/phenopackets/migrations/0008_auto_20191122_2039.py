# Generated by Django 2.2.6 on 2019-11-22 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0038_auto_20191122_2021'),
        ('phenopackets', '0007_auto_20191113_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biosample',
            old_name='biosample_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='gene',
            old_name='gene_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='phenopacket',
            old_name='phenopacket_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='interpretation',
            name='id',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='id',
        ),
        migrations.AlterField(
            model_name='genomicinterpretation',
            name='gene',
            field=models.ForeignKey(blank=True, help_text='The gene contributing to the diagnosis.', null=True, on_delete=django.db.models.deletion.CASCADE, to='phenopackets.Gene', to_field='id'),
        ),
        migrations.AlterField(
            model_name='interpretation',
            name='interpretation_id',
            field=models.CharField(help_text='An arbitrary identifier for the interpretation.', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='interpretation',
            name='phenopacket',
            field=models.ForeignKey(help_text='The subject of this interpretation.', on_delete=django.db.models.deletion.CASCADE, related_name='interpretations', to='phenopackets.Phenopacket', to_field='id'),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='biosample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phenotypic_features', to='phenopackets.Biosample', to_field='id'),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='phenopacket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phenotypic_features', to='phenopackets.Phenopacket', to_field='id'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_id',
            field=models.CharField(help_text='For OBO ontologies, the value of this string MUST always be the official OBO ID, which is always equivalent to the ID prefix in lower case. For other resources use the prefix in identifiers.org.', max_length=200, primary_key=True, serialize=False),
        ),
    ]
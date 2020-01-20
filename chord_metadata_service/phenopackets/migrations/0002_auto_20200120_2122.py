# Generated by Django 2.2.9 on 2020-01-20 21:22

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phenopackets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biosample',
            name='description',
            field=models.CharField(blank=True, help_text='Human-readable, unstructured text describing the biosample or providing additional information.', max_length=200),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='diagnostic_markers',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='A list of ontology terms representing clinically-relevant bio-markers.', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='histological_diagnosis',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term representing a refinement of the clinical diagnosis. Normal samples could be tagged with NCIT:C38757, representing a negative finding', null=True),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='hts_files',
            field=models.ManyToManyField(blank=True, help_text='A list of HTS files derived from the biosample.', related_name='biosample_hts_files', to='phenopackets.HtsFile'),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='id',
            field=models.CharField(help_text='Unique arbitrary, researcher-specified identifier for the biosample.', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='individual',
            field=models.ForeignKey(blank=True, help_text='Identifier for the individual this biosample was sampled from.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biosamples', to='patients.Individual'),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='individual_age_at_collection',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='individual_age_at_collection', null=True),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='procedure',
            field=models.ForeignKey(help_text='A description of a clinical procedure performed on a subject in order to extract a biosample.', on_delete=django.db.models.deletion.CASCADE, to='phenopackets.Procedure'),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='sampled_tissue',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='An ontology term describing the tissue from which the specimen was collected. The use of UBERON is recommended'),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='taxonomy',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term specified when more than one organism may be studied. It is advised that codesfrom the NCBI Taxonomy resource are used, e.g. NCBITaxon:9606 for humans', null=True),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='tumor_grade',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term representing the tumour grade. This should be a child term of NCIT:C28076 (Disease Grade Qualifier) or equivalent', null=True),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='tumor_progression',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term representing if the specimen is from a primary tumour, a metastasis, or a recurrence. There are multiple ways of representing this using ontology terms, and the terms chosen will have a specific meaning that is application specific.', null=True),
        ),
        migrations.AlterField(
            model_name='biosample',
            name='variants',
            field=models.ManyToManyField(blank=True, help_text='A list of variants determined to be present in the biosample.', to='phenopackets.Variant'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='disease_stage',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='A list of terms representing the disease stage. Elements should be derived from child terms of NCIT:C28108 (Disease Stage Qualifier) or equivalent hierarchy from another ontology.', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='disease',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='onset',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A representation of the age of onset of the disease', null=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='term',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text="An ontology term that represents the disease. It's recommended that one of the OMIM, Orphanet, or MONDO ontologies is used for rare human diseases"),
        ),
        migrations.AlterField(
            model_name='disease',
            name='tnm_finding',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='A list of terms representing the tumour TNM score. Elements should be derived from child terms of NCIT:C48232 (Cancer TNM Finding) or equivalent hierarchy from another ontology.', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='alternate_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), blank=True, help_text='A list of identifiers for alternative resources where the gene is used or catalogued.', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='id',
            field=models.CharField(help_text='Official identifier of the gene. It SHOULD be a CURIE identifier with a prefix used by the official organism gene nomenclature committee, e.g. HGNC:347 for humans.', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gene',
            name='symbol',
            field=models.CharField(help_text="A gene's official gene symbol as designated by the organism's gene nomenclature committee, e.g. ETF1 from the HUGO Gene Nomenclature committee.", max_length=200),
        ),
        migrations.AlterField(
            model_name='htsfile',
            name='description',
            field=models.CharField(blank=True, help_text='Human-readable text describing the file.', max_length=200),
        ),
        migrations.AlterField(
            model_name='htsfile',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='htsfile',
            name='genome_assembly',
            field=models.CharField(help_text='Genome assembly ID for the file, e.g. GRCh38.', max_length=200),
        ),
        migrations.AlterField(
            model_name='htsfile',
            name='hts_format',
            field=models.CharField(choices=[('UNKNOWN', 'UNKNOWN'), ('SAM', 'SAM'), ('BAM', 'BAM'), ('CRAM', 'CRAM'), ('VCF', 'VCF'), ('BCF', 'BCF'), ('GVCF', 'GVCF')], help_text="The file's format; one of SAM, BAM, CRAM, VCF, BCF, GVCF, FASTQ, or UNKNOWN.", max_length=200),
        ),
        migrations.AlterField(
            model_name='htsfile',
            name='individual_to_sample_identifiers',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Mapping between individual or biosample IDs and the sample identifier in the HTS file.', null=True),
        ),
        migrations.AlterField(
            model_name='htsfile',
            name='uri',
            field=models.URLField(help_text='A valid URI to the file', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Timestamp specifying when when this object was created.'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='created_by',
            field=models.CharField(help_text='Name of the person who created the phenopacket.', max_length=200),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='external_references',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='A list of external (non-resource) references.', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='resources',
            field=models.ManyToManyField(help_text='A list of resources or ontologies referenced in the phenopacket', to='phenopackets.Resource'),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='submitted_by',
            field=models.CharField(blank=True, help_text='Name of the person who submitted the phenopacket.', max_length=200),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='updates',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='A list of updates to the phenopacket.', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='phenopacket',
            name='biosamples',
            field=models.ManyToManyField(blank=True, help_text='Samples (e.g. biopsies) taken from the individual, if any.', to='phenopackets.Biosample'),
        ),
        migrations.AlterField(
            model_name='phenopacket',
            name='diseases',
            field=models.ManyToManyField(blank=True, help_text='A list of diseases diagnosed in the proband.', to='phenopackets.Disease'),
        ),
        migrations.AlterField(
            model_name='phenopacket',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='phenopacket',
            name='genes',
            field=models.ManyToManyField(blank=True, help_text='Genes deemed to be relevant to the case; application-specific.', to='phenopackets.Gene'),
        ),
        migrations.AlterField(
            model_name='phenopacket',
            name='hts_files',
            field=models.ManyToManyField(blank=True, help_text='A list of HTS files derived from the individual.', to='phenopackets.HtsFile'),
        ),
        migrations.AlterField(
            model_name='phenopacket',
            name='id',
            field=models.CharField(help_text='Unique, arbitrary, researcher-specified identifier for the phenopacket.', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='phenopacket',
            name='meta_data',
            field=models.ForeignKey(help_text='A structured definition of the resources and ontologies used within a phenopacket.', on_delete=django.db.models.deletion.CASCADE, to='phenopackets.MetaData'),
        ),
        migrations.AlterField(
            model_name='phenopacket',
            name='subject',
            field=models.ForeignKey(help_text='A subject of a phenopacket, representing either a human (typically) or another organism.', on_delete=django.db.models.deletion.CASCADE, to='patients.Individual'),
        ),
        migrations.AlterField(
            model_name='phenopacket',
            name='variants',
            field=models.ManyToManyField(blank=True, help_text='A list of variants identified in the proband.', to='phenopackets.Variant'),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='description',
            field=models.CharField(blank=True, help_text='Human-readable text describing the phenotypic feature; NOT for structured text.', max_length=200),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='evidence',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='One or more pieces of evidence that specify how the phenotype was determined.', null=True),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='modifier',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, help_text='A list of ontology terms that provide more expressive / precise descriptions of a phenotypic feature, including e.g. positionality or external factors.', null=True, size=None),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='negated',
            field=models.BooleanField(default=False, help_text='Whether the feature is present (false) or absent (true, feature is negated); default is false.'),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='onset',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term that describes the age at which the phenotypic feature was first noticed or diagnosed, e.g. HP:0003674', null=True),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='pftype',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='An ontology term which describes the phenotype', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='phenotypicfeature',
            name='severity',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term that describes the severity of the condition', null=True),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='body_site',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term that is specified when it is not possible to represent the procedure with a single ontology class', null=True),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='code',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='An ontology term that represents a clinical procedure performed on a subject'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='iri_prefix',
            field=models.URLField(help_text='The IRI prefix, when used with the namespace prefix and an object ID, should resolve the term or object from the resource in question.'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(help_text='The full name of the resource or ontology referred to by the id element.', max_length=200),
        ),
        migrations.AlterField(
            model_name='resource',
            name='namespace_prefix',
            field=models.CharField(help_text='Prefix for objects from this resource. In the case of ontology resources, this should be the CURIE prefix.', max_length=200),
        ),
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.URLField(help_text='Resource URL. In the case of ontologies, this should be an OBO or OWL file. Other resources should link to the official or top-level url.'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='allele',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text="The variant's corresponding allele"),
        ),
        migrations.AlterField(
            model_name='variant',
            name='extra_properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Extra properties that are not supported by current schema.', null=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='zygosity',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology term taken from the Genotype Ontology (GENO) representing the zygosity of the variant', null=True),
        ),
    ]

# Generated by Django 2.2.12 on 2020-05-14 19:41

import chord_metadata_service.restapi.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcode', '0003_auto_20200513_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancercondition',
            name='body_location_code',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='Code for the body location, optionally pre-coordinating laterality or direction. Accepted ontologies: SNOMED CT, ICD-O-3 and others.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='cancercondition',
            name='clinical_status',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A flag indicating whether the condition is active or inactive, recurring, in remission, or resolved (as of the last update of the Condition). Accepted code system: http://terminology.hl7.org/CodeSystem/condition-clinical', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='cancercondition',
            name='condition_code',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='A code describing the type of primary or secondary malignant neoplastic disease.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='cancercondition',
            name='histology_morphology_behavior',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A description of the morphologic and behavioral characteristics of the cancer. Accepted ontologies: SNOMED CT, ICD-O-3 and others.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='cancerrelatedprocedure',
            name='code',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='Code for the procedure performed.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='cancerrelatedprocedure',
            name='target_body_site',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='The body location(s) where the procedure was performed.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='cancerrelatedprocedure',
            name='treatment_intent',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='The purpose of a treatment.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='geneticvariantfound',
            name='genomic_source_class',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology or controlled vocabulary term to identify the genomic class of the specimen being analyzed.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='geneticvariantfound',
            name='method',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology or controlled vocabulary term to identify the method used to perform the genetic test. Accepted value set: NCIT.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='geneticvariantfound',
            name='variant_found_identifier',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='The variation ID assigned by HGVS, for example, 360448 is the identifier for NM_005228.4(EGFR):c.-237A>G (single nucleotide variant in EGFR). Accepted value set: ClinVar.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='geneticvarianttested',
            name='data_value',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology or controlled vocabulary term to identify positive or negative value forthe mutation. Accepted value set: SNOMED CT.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='geneticvarianttested',
            name='method',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology or controlled vocabulary term to identify the method used to perform the genetic test. Accepted value set: NCIT.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='geneticvarianttested',
            name='variant_tested_identifier',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='The variation ID assigned by HGVS, for example, 360448 is the identifier for NM_005228.4(EGFR):c.-237A>G (single nucleotide variant in EGFR).', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='genomicsreport',
            name='specimen_type',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='An ontology or controlled vocabulary term to identify the type of material the specimen contains or consists of. Accepted value set: HL7 Version 2 and Specimen Type.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='genomicsreport',
            name='test_name',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='An ontology or controlled vocabulary term to identify the laboratory test. Accepted value sets: LOINC, GTR.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='labsvital',
            name='tumor_marker_test',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='An ontology or controlled vocabulary term to identify tumor marker test.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:tumor_marker_test', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Tumor marker test schema.', 'properties': {'code': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'data_value': {'anyOf': [{'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, {'$id': 'chord_metadata_service:quantity_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema for the datatype Quantity.', 'properties': {'code': {'type': 'string'}, 'comparator': {'enum': ['<', '>', '<=', '>=', '=']}, 'system': {'format': 'uri', 'type': 'string'}, 'unit': {'type': 'string'}, 'value': {'type': 'number'}}, 'title': 'Quantity schema', 'type': 'object'}, {'$id': 'chord_metadata_service:ratio', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Ratio schema.', 'properties': {'denominator': {'$id': 'chord_metadata_service:quantity_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema for the datatype Quantity.', 'properties': {'code': {'type': 'string'}, 'comparator': {'enum': ['<', '>', '<=', '>=', '=']}, 'system': {'format': 'uri', 'type': 'string'}, 'unit': {'type': 'string'}, 'value': {'type': 'number'}}, 'title': 'Quantity schema', 'type': 'object'}, 'numerator': {'$id': 'chord_metadata_service:quantity_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema for the datatype Quantity.', 'properties': {'code': {'type': 'string'}, 'comparator': {'enum': ['<', '>', '<=', '>=', '=']}, 'system': {'format': 'uri', 'type': 'string'}, 'unit': {'type': 'string'}, 'value': {'type': 'number'}}, 'title': 'Quantity schema', 'type': 'object'}}, 'title': 'Ratio', 'type': 'object'}]}}, 'required': ['code'], 'title': 'Tumor marker test', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='medicationstatement',
            name='medication_code',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='A code for medication. Accepted code systems: Medication Clinical Drug (RxNorm) and other.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='medicationstatement',
            name='termination_reason',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='A code explaining unplanned or premature termination of a course of medication. Accepted ontologies: SNOMED CT.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='medicationstatement',
            name='treatment_intent',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='The purpose of a treatment. Accepted ontologies: SNOMED CT.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, formats=None)]),
        ),
        migrations.AlterField(
            model_name='tnmstaging',
            name='distant_metastases_category',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='Category describing the presence or absence of metastases in remote anatomical locations. Accepted ontologies: SNOMED CT, AJCC and others.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:complex_ontology_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Complex object to combine data value and staging system.', 'properties': {'data_value': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'staging_system': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}}, 'required': ['data_value'], 'title': 'Complex ontology', 'type': 'object'}, formats=['uri'])]),
        ),
        migrations.AlterField(
            model_name='tnmstaging',
            name='primary_tumor_category',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='Category of the primary tumor, based on its size and extent. Accepted ontologies: SNOMED CT, AJCC and others.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:complex_ontology_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Complex object to combine data value and staging system.', 'properties': {'data_value': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'staging_system': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}}, 'required': ['data_value'], 'title': 'Complex ontology', 'type': 'object'}, formats=['uri'])]),
        ),
        migrations.AlterField(
            model_name='tnmstaging',
            name='regional_nodes_category',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='Category of the presence or absence of metastases in regional lymph nodes. Accepted ontologies: SNOMED CT, AJCC and others.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:complex_ontology_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Complex object to combine data value and staging system.', 'properties': {'data_value': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'staging_system': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}}, 'required': ['data_value'], 'title': 'Complex ontology', 'type': 'object'}, formats=['uri'])]),
        ),
        migrations.AlterField(
            model_name='tnmstaging',
            name='stage_group',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='The extent of the cancer in the body, according to the TNM classification system.Accepted ontologies: SNOMED CT, AJCC and others.', validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:complex_ontology_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Complex object to combine data value and staging system.', 'properties': {'data_value': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'staging_system': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}}, 'required': ['data_value'], 'title': 'Complex ontology', 'type': 'object'}, formats=['uri'])]),
        ),
    ]
# Generated by Django 2.2.12 on 2020-05-15 20:45

import chord_metadata_service.restapi.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phenopackets', '0009_auto_20200515_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='biosample',
            name='diagnostic_markers',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of ontology terms representing clinically-relevant bio-markers.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AddField(
            model_name='disease',
            name='disease_stage',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of terms representing the disease stage. Elements should be derived from child terms of NCIT:C28108 (Disease Stage Qualifier) or equivalent hierarchy from another ontology.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AddField(
            model_name='disease',
            name='tnm_finding',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of terms representing the tumour TNM score. Elements should be derived from child terms of NCIT:C48232 (Cancer TNM Finding) or equivalent hierarchy from another ontology.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AddField(
            model_name='metadata',
            name='external_references',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of external (non-resource) references.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:schema_list', '$schema': 'http://json-schema.org/draft-07/schema#', 'items': {'$id': 'chord_metadata_service:external_reference_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'An encoding of information about a reference to an external resource.', 'help': 'An encoding of information about a reference to an external resource.', 'properties': {'description': {'description': 'An application-specific free-text description.', 'help': 'An application-specific free-text description.', 'type': 'string'}, 'id': {'description': 'An application-specific identifier. It is RECOMMENDED that this is a CURIE that uniquely identifies the evidence source when combined with a resource; e.g. PMID:123456 with a resource `pmid`. It could also be a URI or other relevant identifier.', 'help': 'An application-specific identifier. It is RECOMMENDED that this is a CURIE that uniquely identifies the evidence source when combined with a resource; e.g. PMID:123456 with a resource `pmid`. It could also be a URI or other relevant identifier.', 'type': 'string'}}, 'required': ['id'], 'title': 'External reference schema', 'type': 'object'}, 'title': 'Schema list', 'type': 'array'}, formats=None)]),
        ),
        migrations.AddField(
            model_name='metadata',
            name='updates',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of updates to the phenopacket.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:schema_list', '$schema': 'http://json-schema.org/draft-07/schema#', 'items': {'$id': 'chord_metadata_service:update_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'An update event for a record (e.g. a phenopacket.)', 'help': 'An update event for a record (e.g. a phenopacket.)', 'properties': {'comment': {'description': 'Free-text comment about the changes made and/or the reason for the update.', 'help': 'Free-text comment about the changes made and/or the reason for the update.', 'type': 'string'}, 'timestamp': {'description': 'ISO8601 UTC timestamp specifying when when this update occurred.', 'format': 'date-time', 'help': 'Timestamp specifying when when this update occurred.', 'type': 'string'}, 'updated_by': {'description': 'Information about the person/organization/network that performed the update.', 'help': 'Information about the person/organization/network that performed the update.', 'type': 'string'}}, 'required': ['timestamp', 'comment'], 'title': 'Updates schema', 'type': 'object'}, 'title': 'Schema list', 'type': 'array'}, formats=['date-time'])]),
        ),
        migrations.AddField(
            model_name='phenotypicfeature',
            name='modifier',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='A list of ontology terms that provide more expressive / precise descriptions of a phenotypic feature, including e.g. positionality or external factors.', null=True, validators=[chord_metadata_service.restapi.validators.JsonSchemaValidator({'$id': 'chord_metadata_service:ontology_class_list_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'description': 'Ontology class list', 'items': {'$id': 'chord_metadata_service:ontology_class_schema', '$schema': 'http://json-schema.org/draft-07/schema#', 'additionalProperties': False, 'description': 'Schema to describe terms from ontologies.', 'properties': {'id': {'description': 'CURIE style identifier.', 'type': 'string'}, 'label': {'description': 'Human-readable class name.', 'type': 'string'}}, 'required': ['id', 'label'], 'title': 'Ontology class schema', 'type': 'object'}, 'title': 'Ontology class list', 'type': 'array'}, formats=None)]),
        ),
    ]

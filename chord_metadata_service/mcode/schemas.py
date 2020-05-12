from chord_metadata_service.restapi.schema_utils import customize_schema
from chord_metadata_service.restapi.schemas import ONTOLOGY_CLASS, ONTOLOGY_CLASS_LIST, EXTRA_PROPERTIES_SCHEMA
from chord_metadata_service.restapi.description_utils import describe_schema
from .descriptions import *
from chord_metadata_service.phenopackets.schemas import PHENOPACKET_GENE_SCHEMA


################################## mCode/FHIR based schemas ##################################

### FHIR datatypes

# FHIR Quantity https://www.hl7.org/fhir/datatypes.html#Quantity
QUANTITY = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "chord_metadata_service:quantity_schema",
    "title": "Quantity schema",
    "description": "Schema for the datatype Quantity.",
    "type": "object",
    "properties": {
        "value": {
            "type": "number"
        },
        "comparator": {
            "enum": ["<", ">", "<=", ">=", "="]
        },
        "unit": {
            "type": "string"
        },
        "system": {
            "type": "string",
            "format": "uri"
        },
        "code": {
            "type": "string"
        }
    },
    "additionalProperties": False
}


# FHIR CodeableConcept https://www.hl7.org/fhir/datatypes.html#CodeableConcept
CODEABLE_CONCEPT = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "chord_metadata_service:codeable_concept_schema",
    "title": "Codeable Concept schema",
    "description": "Schema for the datatype Concept.",
    "type": "object",
    "properties": {
        "coding": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "system": {"type": "string", "format": "uri"},
                    "version": {"type": "string"},
                    "code": {"type": "string"},
                    "display": {"type": "string"},
                    "user_selected": {"type": "boolean"}
                }
            }
        },
        "text": {
            "type": "string"
        }
    },
    "additionalProperties": False
}


# FHIR Period https://www.hl7.org/fhir/datatypes.html#Period
PERIOD = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "chord_metadata_service:period_schema",
    "title": "Period",
    "description": "Period schema.",
    "type": "object",
    "properties": {
        "start": {
            "type": "string",
            "format": "date-time"
        },
        "end": {
            "type": "string",
            "format": "date-time"
        }
    },
    "additionalProperties": False
}


# FHIR Ratio https://www.hl7.org/fhir/datatypes.html#Ratio
RATIO = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "chord_metadata_service:ratio",
    "title": "Ratio",
    "description": "Ratio schema.",
    "type": "object",
    "properties": {
        "numerator": QUANTITY,
        "denominator": QUANTITY
    },
    "additionalProperties": False
}


### FHIR based mCode elements

TIME_OR_PERIOD = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "chord_metadata_service:time_or_period",
    "title": "Time of Period",
    "description": "Time of Period schema.",
    "type": "object",
    "properties": {
        "value": {
            "anyOf": [
                {"type": "string", "format": "date-time"},
                PERIOD
            ]
        }
    },
    "additionalProperties": False
}

# TODO this is definitely should be changed, fhir datatypes are too complex use Ontology_ class
COMPLEX_ONTOLOGY = customize_schema(
    first_typeof=ONTOLOGY_CLASS,
    second_typeof=ONTOLOGY_CLASS,
    first_property="data_value",
    second_property="staging_system",
    schema_id="chord_metadata_service:complex_ontology_schema",
    title="Complex ontology",
    description="Complex object to combine data value and staging system.",
    required=["data_value"]
)

# TODO this is definitely should be changed, fhir datatypes are too complex use Ontology_ class
TUMOR_MARKER_TEST = customize_schema(
    first_typeof=ONTOLOGY_CLASS,
    second_typeof={
       "anyOf": [
           ONTOLOGY_CLASS,
           QUANTITY,
           RATIO
       ]
    },
    first_property="code",
    second_property="data_value",
    schema_id="chord_metadata_service:tumor_marker_test",
    title="Tumor marker test",
    description="Tumor marker test schema.",
    required=["code"]
)

############################## Metadata service mCode based schemas ##############################


MCODE_GENETIC_VARIANT_TESTED_SCHEMA = describe_schema({
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "gene_studied": {
            "type": "string"
        },
        "method": ONTOLOGY_CLASS,
        "variant_tested_identifier": ONTOLOGY_CLASS,
        "variant_tested_hgvs_name": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "variant_tested_description": {
            "type": "string"
        },
        "data_value": ONTOLOGY_CLASS,
        "extra_properties": EXTRA_PROPERTIES_SCHEMA
    },
    "required": ["id"]
}, GENETIC_VARIANT_TESTED)

MCODE_GENETIC_VARIANT_FOUND_SCHEMA = describe_schema({
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "method": ONTOLOGY_CLASS,
        "variant_found_identifier": ONTOLOGY_CLASS,
        "variant_found_hgvs_name": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "variant_found_description": {
            "type": "string"
        },
        "genomic_source_class": ONTOLOGY_CLASS,
        "extra_properties": EXTRA_PROPERTIES_SCHEMA
    },
    "required": ["id"]
}, GENETIC_VARIANT_FOUND)

MCODE_GENOMICS_REPORT_SCHEMA = describe_schema({
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "test_name": ONTOLOGY_CLASS,
        "performing_organization_name": {
            "type": "string"
        },
        "specimen_type": ONTOLOGY_CLASS,
        "genetic_variant_tested": {
            "type": "array",
            "items": {
                "string"
            }
        },
        "genetic_variant_found": {
            "type": "array",
            "items": {
                "string"
            }
        },
        "extra_properties": EXTRA_PROPERTIES_SCHEMA
    },
    "required": ["id", "test_name"]
}, GENOMICS_REPORT)

MCODE_LABS_VITAL_SCHEMA = describe_schema({
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "subject": {
            "type": "string"
        },
        "body_height": QUANTITY,
        "body_weight": QUANTITY,
        "cbc_with_auto_differential_panel": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "comprehensive_metabolic_2000": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "blood_pressure_diastolic": QUANTITY,
        "blood_pressure_systolic": QUANTITY,
        "tumor_marker_test": TUMOR_MARKER_TEST,
        "extra_properties": EXTRA_PROPERTIES_SCHEMA
    },
    "required": ["id", "individual", "body_height", "body_weight", "tumor_marker_test"]
}, LABS_VITAL)

# TODO check required inb data dictionary
MCODE_CANCER_CONDITION_SCHEMA = describe_schema({
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "condition_type": {
            "type": "string",
            "enum": [
                "primary",
                "secondary"
            ]
        },
        "body_location_code": ONTOLOGY_CLASS_LIST,
        "clinical_status": ONTOLOGY_CLASS,
        "condition_code": ONTOLOGY_CLASS,
        "date_of_diagnosis": {
            "type": "string",
            "format": "date-time"
        },
        "histology_morphology_behavior": ONTOLOGY_CLASS,
        "extra_properties": EXTRA_PROPERTIES_SCHEMA
    },
    "required": ["id", "condition_type", "condition_code"]
}, LABS_VITAL)


MCODE_TNM_STAGING_SCHEMA = describe_schema({
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "tnm_type": {
            "type": "string",
            "enum": [
                "clinical",
                "pathologic"
            ]
        },
        "stage_group": COMPLEX_ONTOLOGY,
        "primary_tumor_category": COMPLEX_ONTOLOGY,
        "regional_nodes_category": COMPLEX_ONTOLOGY,
        "distant_metastases_category": COMPLEX_ONTOLOGY,
        "cancer_condition": {
            "type": "string"
        },
        "extra_properties": EXTRA_PROPERTIES_SCHEMA
    },
    "required": [
        "id",
        "tnm_type",
        "stage_group",
        "primary_tumor_category",
        "regional_nodes_category",
        "distant_metastases_category",
        "cancer_condition"
    ]
}, TNM_STAGING)


MCODE_CANCER_RELATED_PROCEDURE_SCHEMA = describe_schema({
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "procedure_type": {
            "type": "string",
            "enum": [
                "radiation",
                "surgical"
            ]
        },
        "code": ONTOLOGY_CLASS,
        "occurence_time_or_period": TIME_OR_PERIOD,
        "target_body_site": ONTOLOGY_CLASS_LIST,
        "treatment_intent": ONTOLOGY_CLASS,
        "extra_properties": EXTRA_PROPERTIES_SCHEMA
    },
    "required": ["id", "procedure_type", "code", "occurence_time_or_period"]
}, CANCER_RELATED_PROCEDURE)


MCODE_MEDICATION_STATEMENT_SCHEMA = describe_schema({
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "medication_code": ONTOLOGY_CLASS,
        "termination_reason": ONTOLOGY_CLASS_LIST,
        "treatment_intent": ONTOLOGY_CLASS,
        "start_date": {
            "type": "string",
            "format": "date-time"
        },
        "end_date": {
            "type": "string",
            "format": "date-time"
        },
        "date_time": {
            "type": "string",
            "format": "date-time"
        },

        "extra_properties": EXTRA_PROPERTIES_SCHEMA
    },
    "required": ["id", "medication_code"]
}, MEDICATION_STATEMENT)

# TODO add subject fk to individual
MCODE_SCHEMA = describe_schema({
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "chord_metadata_service:mcode_schema",
    "title": "Metadata service customized mcode schema",
    "description": "Schema for describe mcode data elements in metadata service.",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "genomics_report": MCODE_GENOMICS_REPORT_SCHEMA,
        "cancer_condition": MCODE_CANCER_CONDITION_SCHEMA,
        "cancer_related_procedures": MCODE_CANCER_RELATED_PROCEDURE_SCHEMA,
        "medication_statement": MCODE_MEDICATION_STATEMENT_SCHEMA,
        "extra_properties": EXTRA_PROPERTIES_SCHEMA
    }
}, MCODEPACKET)

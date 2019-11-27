VALID_PROCEDURE_1 = {
    "code": {
        "id": "NCIT:C28743",
        "label": "Punch Biopsy"
    },
    "body_site": {
        "id": "UBERON:0003403",
        "label": "skin of forearm"
    }
}


VALID_META_DATA_1 = {
    "created_by": "David Lougheed",
    "submitted_by": "David Lougheed"
}


def valid_biosample_1(individual, procedure):
    return dict(
        id='biosample_id:1',
        individual=individual,
        sampled_tissue={
            "id": "UBERON_0001256",
            "label": "wall of urinary bladder"
        },
        description='This is a test biosample.',
        taxonomy={
            "id": "NCBITaxon:9606",
            "label": "Homo sapiens"
        },
        individual_age_at_collection='P52Y2M',
        histological_diagnosis={
            "id": "NCIT:C39853",
            "label": "Infiltrating Urothelial Carcinoma"
        },
        tumor_progression={
            "id": "NCIT:C84509",
            "label": "Primary Malignant Neoplasm"
        },
        tumor_grade={
            "id": "NCIT:C48766",
            "label": "pT2b Stage Finding"
        },
        diagnostic_markers=[
            {
                "id": "NCIT:C49286",
                "label": "Hematology Test"
            },
            {
                "id": "NCIT:C15709",
                "label": "Genetic Testing"
            }
        ],
        procedure=procedure,
        is_control_sample=True
    )


def valid_biosample_2(individual, procedure):
    return dict(
        id='biosample_id:2',
        individual=individual,
        sampled_tissue={
            "id": "UBERON_0001256",
            "label": "urinary bladder"
        },
        description='This is a test biosample.',
        taxonomy={
            "id": "NCBITaxon:9606",
            "label": "Homo sapiens"
        },
        individual_age_at_collection='P52Y2M',
        histological_diagnosis={
            "id": "NCIT:C39853",
            "label": "Infiltrating Urothelial Carcinoma"
        },
        tumor_progression={
            "id": "NCIT:C3677",
            "label": "Benign Neoplasm"
        },
        tumor_grade={
            "id": "NCIT:C48766",
            "label": "pT2b Stage Finding"
        },
        diagnostic_markers=[
            {
                "id": "NCIT:C49286",
                "label": "Hematology Test"
            },
            {
                "id": "NCIT:C15709",
                "label": "Genetic Testing"
            }
        ],
        procedure=procedure,
        is_control_sample=True
    )

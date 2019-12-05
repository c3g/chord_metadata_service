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


VALID_PROCEDURE_2 = {
    "code": {
        "id": "NCIT:C28743",
        "label": "Punch Biopsy"
    },
    "body_site": {
        "id": "UBERON:0004263",
        "label": "upper arm skin"
    }
}


VALID_META_DATA_1 = {
    "created_by": "David Lougheed",
    "submitted_by": "David Lougheed"
}


VALID_META_DATA_2 = {
    "created_by": "Ksenia Zaytseva",
    "submitted_by": "Ksenia Zaytseva"
}


VALID_INDIVIDUAL_1 = {
    "id": "patient:1",
    "date_of_birth": "1967-01-01",
    "sex": "MALE"
}


VALID_INDIVIDUAL_2 = {
    "id": "patient:2",
    "date_of_birth": "1978-01-01",
    "sex": "FEMALE"
}


VALID_HTS_FILE = {
    "uri": "https://data.example/genomes/germline_wgs.vcf.gz",
    "description": "Matched normal germline sample",
    "hts_format": "VCF",
    "genome_assembly": "GRCh38",
    "individual_to_sample_identifiers": {
      "patient:1": "NA12345"
    },
    "extra_properties": {
        "comment": "test data"
    }
}


VALID_GENE_1 = {
  "id": "HGNC:347",
  "alternate_ids": ["ensembl:ENSRNOG00000019450", "ncbigene:307503"],
  "symbol": "ETF1",
  "extra_properties": {
    "comment": "test data"
  }
}


DUPLICATE_GENE_2 = {
  "id": "HGNC:347",
  "symbol": "DYI"
}


VALID_VARIANT_1 = {
    "allele_type": "spdiAllele",
    "allele": {
      "id": "clinvar:13294",
      "seq_id": "NC_000010.10",
      "position": 123256214,
      "deleted_sequence": "T",
      "inserted_sequence": "G"
    },
    "zygosity": {
      "id": "NCBITaxon:9606",
      "label": "human"
    },
    "extra_properties": {
        "comment": "test data"
    }
}


VALID_DISEASE_1 = {
    "term": {
        "id": "OMIM:164400",
        "label": "Spinocerebellar ataxia 1"
    },
    "onset": {
        "age": "P25Y3M2D"
    },
    "disease_stage": [
        {
        "id": "NCIT:C28091",
        "label": "Gleason Score 7"
        }
    ],
    "extra_properties": {
        "comment": "test data"
    }
}


VALID_RESOURCE_1 = {
    "id": "so",
    "name": "Sequence types and features",
    "url": "http://purl.obolibrary.org/obo/so.owl",
    "version": "2015-11-24",
    "namespace_prefix": "SO",
    "iri_prefix": "http://purl.obolibrary.org/obo/SO_"
}


VALID_RESOURCE_2 = {
    "id": "hgnc",
    "name": "HUGO Gene Nomenclature Committee",
    "url": "https://www.genenames.org",
    "version": "2019-08-08",
    "namespace_prefix": "HGNC",
    "iri_prefix": "https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/"
}


DUPLICATE_RESOURCE_3 = {
    "id": "hgnc",
    "name": "HUGO Gene Nomenclature Committee",
    "url": "https://www.genenames.org",
    "version": "2019-08-08",
    "namespace_prefix": "HGNC"
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


def valid_phenotypic_feature(biosample=None, phenopacket=None):
    return dict(
        description='This is a test phenotypic feature',
        pftype={
            "id": "HP:0000520",
            "label": "Proptosis" 
        },
        negated=True,
        severity={
            "id": "HP: 0012825",
            "label": "Mild"
        },
        modifier=[
            {
            "id": "HP: 0012825 ",
            "label": "Mild"
            },
            {
            "id": "HP: 0012823 ",
            "label": "Semi-mild"
            }
        ],
        onset={
            "id": "HP:0003577",
            "label": "Congenital onset"
        },
        evidence={
            "evidence_code": {
                "id": "ECO:0006017",
                "label": "Author statement from published clinical study used in manual assertion"
            },
            "reference": {
                "id": "PMID:30962759",
                "description": "Recurrent Erythema Nodosum in a Child with a SHOC2 Gene Mutation"
            }
        },
        extra_properties={
            "comment": "test data"
        },
        biosample=biosample,
        phenopacket=phenopacket
        )


def invalid_phenotypic_feature():
    return dict(
        description='This is a test phenotypic feature',
        negated=True,
        severity={
            "id": "HP: 0012825",
            "label": "Mild"
        },
        modifier=[
            {
            "label": "Mild"
            },
            {
            "id": "HP: 0012823 "
            }
        ],
        onset={
            "id": "HP:0003577",
            "label": "Congenital onset"
        },
        evidence={
            "evidence_code": {
                "id": "ECO:0006017",
                "label": "Author statement from published clinical study used in manual assertion"
            },
            "reference": {
                "id": "PMID:30962759",
                "description": "Recurrent Erythema Nodosum in a Child with a SHOC2 Gene Mutation"
            }
        },
        extra_properties={
            "comment": "test data"
        }
        )


def valid_genomic_interpretation(gene=None, variant=None):
    return dict(
            status='CANDIDATE',
            gene=gene,
            variant=variant,
            extra_properties={
                "comment": "test data"
            }
        )


def valid_diagnosis(disease):
    return dict(
        disease=disease,
        extra_properties={
            "comment": "test data"
        }
        )


def valid_interpretation(phenopacket, meta_data):
    return dict(
        id='interpretation:1',
        resolution_status='IN_PROGRESS',
        phenopacket=phenopacket,
        meta_data=meta_data,
        extra_properties={
            "comment": "test data"
        }
        )
import logging
from chord_metadata_service.patients.models import Individual
from .models import *


logger = logging.getLogger("mcode_ingest")
logger.setLevel(logging.INFO)


def ingest_mcodepacket(mcodepacket_data, table_id):
    """ Ingests a single mcodepacket in mcode app and patients' metadata int patients app."""

    new_mcodepacket = {"id": mcodepacket_data["id"]}
    subject = mcodepacket_data["subject"]
    genomics_report_data = mcodepacket_data.get("genomics_report", None)
    cancer_condition_data = mcodepacket_data.get("cancer_condition", None)
    cancer_related_procedures = mcodepacket_data.get("cancer_related_procedures", None)
    medication_statement_data = mcodepacket_data.get("medication_statement", None)
    date_of_death_data = mcodepacket_data.get("date_of_death", None)
    cancer_disease_status_data = mcodepacket_data.get("cancer_disease_status", None)
    tumor_markers = mcodepacket_data.get("tumor_marker", None)

    # get and create Patient
    if subject:
        subject, _ = Individual.objects.get_or_create(**subject)
        new_mcodepacket["subject"] = subject.id

    if genomics_report_data:
        # don't have data for genomics report yet
        pass

    # get and create CancerCondition
    cancer_conditions = []
    if cancer_condition_data:
        for cc in cancer_condition_data:

            cancer_condition, _ = CancerCondition.objects.get_or_create(
                id=cc["id"],
                code=cc["code"],
                condition_type=cc["condition_type"],
                clinical_status=cc.get("clinical_status", None),
                verification_status=cc.get("verification_status", None),
                date_of_diagnosis=cc.get("date_of_diagnosis", None),
                body_site=cc.get("body_site", None),
                laterality=cc.get("laterality", None),
                histology_morphology_behavior=cc.get("histology_morphology_behavior", None)
            )
            print(f"CANCER CONDITION {cancer_condition}")
            cancer_conditions.append(cancer_condition.id)
            if "tnm_staging" in cc:
                for tnms in cc["tnm_staging"]:
                    tnm_staging, _ = TNMStaging.objects.get_or_create(
                        id=tnms["id"],
                        cancer_condition=cancer_condition,
                        stage_group=tnms["stage_group"],
                        tnm_type=tnms["tnm_type"],
                        primary_tumor_category=tnms.get("primary_tumor_category", None),
                        regional_nodes_category=tnms.get("regional_nodes_category", None),
                        distant_metastases_category=tnms.get("distant_metastases_category", None)
                    )

    # get and create Cancer Related Procedure
    crprocedures = []
    if cancer_related_procedures:
        for crp in cancer_related_procedures:
            cancer_related_procedure, _ = CancerRelatedProcedure.objects.get_or_create(
                id=crp["id"],
                code=crp["code"],
                procedure_type=crp["procedure_type"],
                body_site= crp.get("body_site", None),
                laterality=crp.get("laterality", None),
                treatment_intent=crp.get("treatment_intent", None),
                reason_code=crp.get("reason_code", None),
                extra_properties=crp.get("extra_properties", None)
            )
            crprocedures.append(cancer_related_procedure.id)
            if "reason_reference" in crp:
                related_cancer_conditions = []
                for rr_id in crp["reason_reference"]:
                    print(f"REASON REFERENCE CANCER CONDITION {rr_id}")
                    condition = CancerCondition.objects.get(id=rr_id)
                    related_cancer_conditions.append(condition)
                cancer_related_procedure.reason_reference.set(related_cancer_conditions)

    # get and create CancerCondition
    if medication_statement_data:
        medication_statement, _ = MedicationStatement.objects.get_or_create(
            id=medication_statement_data["id"],
            medication_code=medication_statement_data["medication_code"]
        )
        new_mcodepacket["medication_statement"] = medication_statement

    # get date of death
    if date_of_death_data:
        new_mcodepacket["date_of_death"] = date_of_death_data

    # get cancer disease status
    if cancer_disease_status_data:
        new_mcodepacket["cancer_disease_status"] = cancer_disease_status_data

    # get tumor marker
    if tumor_markers:
        for tm in tumor_markers:
            tumor_marker, _ = LabsVital.objects.get_or_create(
                id=tm["id"],
                tumor_marker_code=tm["tumor_marker_code"],
                tumor_marker_data_value=tm.get("tumor_marker_data_value", None),
                individual=Individual.objects.get(id=tm["individual"])
            )

    mcodepacket = MCodePacket(
        id=new_mcodepacket["id"],
        subject=Individual.objects.get(id=new_mcodepacket["subject"]),
        genomics_report=new_mcodepacket.get("genomics_report", None),
        medication_statement=new_mcodepacket.get("medication_statement", None),
        date_of_death=new_mcodepacket.get("date_of_death", ""),
        cancer_disease_status=new_mcodepacket.get("cancer_disease_status", None),
        table_id=table_id
    )
    mcodepacket.save()
    if cancer_conditions:
        mcodepacket.cancer_condition.set(cancer_conditions)
    if crprocedures:
        mcodepacket.cancer_related_procedures.set(crprocedures)

    return mcodepacket

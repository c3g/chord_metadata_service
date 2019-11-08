# Utils for converting data between formats


def camel_case_field_names(string):
	""" Function to convert snake_case field names to camelCase """

	if '_' in string:
		splitted = string.split('_')
		capitilized = []
		capitilized.append(splitted[0])
		for each in splitted[1:]:
			capitilized.append(each.title())
		return ''.join(capitilized)
	return string


def convert_to_fhir(individual_data):
	""" Transform individual data to Patient FHIR record """
	fhir_record = {}
	fhir_record['resourceType'] = 'Patient'
	# mapping for basic Patient attributes
	mapping = {
	'individual_id': 'identifier',
	'date_of_birth': 'birthDate',
	'sex': 'gender',
	'active': 'active',
	'deceased': 'deceased',
	'address_postal_code': 'addresPostalCode',
	'race': 'race',
	'ethnicity': 'ethnicity'
	}
	for field in mapping.keys():
		if field in individual_data.keys():
			fhir_record[mapping.get(field)] = individual_data.get(field, None)
	# mapping for biosamples assosiated with this patient
	if 'biosamples' in individual_data.keys():
		fhir_record['biosamples'] = []
		for sample in individual_data.get('biosamples', None):
			biosample_record = {}
			biosample_record['resourceType'] = 'Specimen'
			biosample_record['identifier'] = sample.get('biosample_id', None)
			biosample_record['parent'] = {}
			biosample_record['parent']['reference'] = {}
			biosample_record['parent']['reference']['reference'] = sample.get('sampled_tissue').get('id', None)
			biosample_record['parent']['reference']['display'] = sample.get('sampled_tissue').get('label', None)
			# mapping for phenotypic_features related to each biosample
			if 'phenotypic_features' in sample.keys():
				biosample_record['phenotypicFeatures'] = []
				for feature in sample.get('phenotypic_features'):
					feature_record = {}
					feature_record['resourceType'] = 'Condition'
					if 'id' in feature.keys():
						feature_record['identifier'] = feature.get('id', None)
					if 'description' in feature.keys():
						feature_record['text'] = feature.get('description', None)
					if 'type' in feature.keys():
						feature_record['code'] = {}
						feature_record['code']['coding'] = []
						ftype = {}
						ftype['code'] = feature.get('type').get('id', None)
						ftype['display'] = feature.get('type').get('label', None)
						feature_record['code']['coding'].append(ftype)
					biosample_record['phenotypicFeatures'].append(feature_record)
			# mapping for procedure relared to each biosample
			if 'procedure' in sample.keys():
				procedure = sample.get('procedure')
				biosample_record['procedure'] = {}
				biosample_record['procedure']['resourceType'] = 'Procedure'
				biosample_record['procedure']['code'] = {}
				biosample_record['procedure']['code']['coding'] = []
				code = {}
				code['code'] = procedure.get('code').get('id', None)
				code['display'] = procedure.get('code').get('label', None)
				biosample_record['procedure']['code']['coding'].append(code)
				biosample_record['procedure']['code']['bodySite'] = []
				body_site = {}
				body_site['code'] = procedure.get('body_site').get('id', None)
				body_site['display'] = procedure.get('body_site').get('label', None)
				biosample_record['procedure']['code']['bodySite'].append(body_site)
			# all these elements are represented by FHIR Class CodeableConcept
			# and have the same schema
			codeable_concepts = [
				'taxonomy', 'histological_diagnosis',
				'tumor_progression', 'tumor_grade',
				'diagnostic_markers'
				]
			for concept in codeable_concepts:
				if concept in sample.keys():
					concept_data = sample.get(concept)
					concept_field_name = camel_case_field_names(concept)
					biosample_record[concept_field_name] = {}
					biosample_record[concept_field_name]['resourceType'] = 'CodeableConcept'
					biosample_record[concept_field_name]['coding'] = []
					coding = {}
					if isinstance(concept_data, list):
						for item in concept_data:
							coding['code'] = item.get('id', None)
							coding['display'] = item.get('label', None)
							biosample_record[concept_field_name]['coding'].append(coding)
					else:
						coding['code'] = concept_data.get('id', None)
						coding['display'] = concept_data.get('label', None)
						biosample_record[concept_field_name]['coding'].append(coding)

			fhir_record['biosamples'].append(biosample_record)

	return fhir_record
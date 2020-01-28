from rest_framework import viewsets, pagination
from .serializers import *
from .models import *
from rest_framework.settings import api_settings
from chord_metadata_service.restapi.api_renderers import (
    FHIRRenderer, PhenopacketsRenderer)


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 10000


class IndividualViewSet(viewsets.ModelViewSet):
    """
    get:
    Return a list of all existing individuals

    post:
    Create a new individual

    """
    queryset = Individual.objects.all().prefetch_related(
        "biosamples",
        "phenopackets__meta_data",
        "phenopackets__biosamples__phenotypic_features",
        "phenopackets__genes",
        "phenopackets__variants",
        "phenopackets__diseases",
        "phenopackets__hts_files",
        "phenopackets__phenotypic_features",
    ).order_by("id")
    serializer_class = IndividualSerializer
    pagination_class = LargeResultsSetPagination
    renderer_classes = tuple(
        api_settings.DEFAULT_RENDERER_CLASSES
        ) + (FHIRRenderer, PhenopacketsRenderer)

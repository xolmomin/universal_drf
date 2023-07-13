from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, SuggesterFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from apps.documents import ProductDocument
from apps.serializers import ProductDocumentSerializer


class ProductDocumentViewSet(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductDocumentSerializer

    filter_backends = [SearchFilterBackend, SuggesterFilterBackend]
    search_fields = (
        'name',
        'description',
    )
    suggester_fields = {
        'name': {
            'field': 'name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }
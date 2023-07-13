from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from apps.documents import ProductDocument


class ProductDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ProductDocument
        fields = ('id', 'name', 'description')

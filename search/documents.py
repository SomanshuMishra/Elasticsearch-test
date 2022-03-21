from pyexpat import model
from django_elasticsearch_dsl import Document ,fields
from django_elasticsearch_dsl.registries import registry
from search.models import importkey


@registry.register_document
class ImportKeyDocument(Document):
    
    print('document')
    class Index:
        name = 'importkey'
    
    class Django:
        model = importkey
        fields = [
            'BOL',
            'HOUSE_BILL',
            'SUB_HOUSE_BILL',
            'VOYAGE_NUMBER',
            'BILL_TYPE',
            'manifest',
        ]
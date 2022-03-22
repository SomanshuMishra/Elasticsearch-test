from pyexpat import model
from django_elasticsearch_dsl import Document ,fields
from django_elasticsearch_dsl.registries import registry
from search.models import importkey


@registry.register_document
class ImportKeyDocument(Document):
    
    print('document')
    class Index:
        name = 'importkey'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    
    class Django:
        model = importkey
        fields = [
                        'BOL',
            'HOUSE_BILL',
            'SUB_HOUSE_BILL',
            'VOYAGE_NUMBER',
            'BILL_TYPE',
            'manifest',
            'Trade_Update_Date',
            'RUN_DATE',
            'CARRIER_CODE',
            'Vessel_Country_Code',
            'Vessell_Name',
            'Port_of_Unlading',
            'Estimated_Arrival_Date',
            'Foreign_Port_of_Lading_Qualifier',
            'Foreign_Port_of_Lading',
            'Manifest_Quanity',
            'Manifest_Unit',
            'Weight',
            'Weight_Unit',
            'Measurement',
            'Measurement_Unit',
            'Record_Status_Indicator',
            'Place_of_Receipt',
            'Port_of_Destination',
            'Foreign_Port_of_Destination_Qualifier',
            'Foreign_Port_of_Destination',
            'Conveyance_ID_Qualifier',
            'Conveyance_ID',
            'IN_BOND_entry_type',
            'Mode_of_Transportation',
            'Actual_Arrival_Date',
            'NOTIFY_PARTIES',
            'shipper_name',
            'Shipper_Address',
            'country_code',
            'Shipper_Contact_Info',
            'Consignee_Name',
            'Consignee_Address',
            # Country_Code
            'Consignee_Contact_Info',
            'Notify_Party_Name',
            'Notify_Address',
            'Country_Code',
            'Notify_Contact_Info',
            'Container_Number',
            'Container_Description_Sequence_Number',
            'piece_count',
            'Cargo_Description',
            'Tariff_Informtion_from_record_61',
            'Container_Info_from_Type_20_Record',

        ]
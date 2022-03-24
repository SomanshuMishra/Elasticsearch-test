from django.contrib import admin
from .models import importkey ,trial ,n 
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(importkey)
@admin.register(importkey)
class ImportKeyAdmin(ImportExportModelAdmin):
    # list_display = '_'
    pass
# @admin.register(trial_importkey)
# class ImportKeyAdmin(ImportExportModelAdmin):
#     # list_display = '_'
#     pass
@admin.register(trial)
class TrialAdmin(ImportExportModelAdmin):
    # list_display = 'BOL,HOUSE_BILL,SUB_HOUSE_BILL,VOYAGE_NUMBER,BILL_TYPE,manifest,Trade_Update_Date,RUN_DATE,CARRIER_CODE,Vessel_Country_Code,Vessell_Name,Port_of_Unlading,Estimated_Arrival_Date,Foreign_Port_of_Lading_Qualifier,Foreign_Port_of_Lading,Manifest_Quanity,Manifest_Unit,Weight,Weight_Unit,Measurement,Measurement_Unit,Record_Status_Indicator,Place_of_Receipt,Port_of_Destination,Foreign_Port_of_Destination_Qualifier,Foreign_Port_of_Destination,Conveyance_ID_Qualifier,Conveyance_ID,IN_BOND_entry_type,Mode_of_Transportation,Actual_Arrival_Date,NOTIFY_PARTIES,shipper_name,Shipper_Address,country_code,Shipper_Contact_Info,Consignee_Name,Consignee_Address,Country_Code,Consignee_Contact_Info,Notify_Party_Name,Notify_Address,Country_Code,Notify_Contact_Info,Container_Number,Container_Description_Sequence_Number,piece_count,Cargo_Description,Tariff_Informtion_from_record_61	'
    pass
@admin.register(n)
class nAdmin(ImportExportModelAdmin):
    # list_display = 'BOL,HOUSE_BILL,SUB_HOUSE_BILL,VOYAGE_NUMBER,BILL_TYPE,manifest,Trade_Update_Date,RUN_DATE,CARRIER_CODE,Vessel_Country_Code,Vessell_Name,Port_of_Unlading,Estimated_Arrival_Date,Foreign_Port_of_Lading_Qualifier,Foreign_Port_of_Lading,Manifest_Quanity,Manifest_Unit,Weight,Weight_Unit,Measurement,Measurement_Unit,Record_Status_Indicator,Place_of_Receipt,Port_of_Destination,Foreign_Port_of_Destination_Qualifier,Foreign_Port_of_Destination,Conveyance_ID_Qualifier,Conveyance_ID,IN_BOND_entry_type,Mode_of_Transportation,Actual_Arrival_Date,NOTIFY_PARTIES,shipper_name,Shipper_Address,country_code,Shipper_Contact_Info,Consignee_Name,Consignee_Address,Country_Code,Consignee_Contact_Info,Notify_Party_Name,Notify_Address,Country_Code,Notify_Contact_Info,Container_Number,Container_Description_Sequence_Number,piece_count,Cargo_Description,Tariff_Informtion_from_record_61	'
    pass

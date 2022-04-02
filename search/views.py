from multiprocessing.sharedctypes import Value
from re import search
from tkinter.tix import AUTO
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from search.models import importkey
from search.serializer import ImportKeySerializer
from search.documents import ImportKeyDocument
from django.http import HttpResponse
from elasticsearch_dsl import Q 
from django.http import JsonResponse
import math
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
# Create your views here.
import time
from datetime import datetime


class SearchImportKey(APIView,LimitOffsetPagination):
    serializer_class = ImportKeySerializer
    search_document = ImportKeyDocument
    def get(self,request):
        try:
            query = request.GET['q']
            page = int(request.GET['page'])
            q = Q(
                'multi_match',
                query=query,
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
                    # 'Port_of_Unlading',
                    # 'Estimated_Arrival_Date',
                    # 'Foreign_Port_of_Lading_Qualifier',
                    # 'Foreign_Port_of_Lading',
                    # 'Manifest_Quanity',
                    # 'Manifest_Unit',
                    # 'Weight',
                    # 'Weight_Unit',
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
                    # 'Container_Number',
                    'Container_Description_Sequence_Number',
                    # 'piece_count',
                    'Cargo_Description',
                    'Tariff_Informtion_from_record_61',
                    'Container_Info_from_Type_20_Record',

                ],
                # fuzziness = "AUTO"    
            )
            search = self.search_document.search().query(q)[:1000]
            counts = search.count()
            if page>1:
                start = page*1000
                end = start+1000
                search = self.search_document.search().query(q)[start:end]
                

            response = search.execute()
            serializer = self.serializer_class(response, many=True)
            return JsonResponse({'Total Rows':counts,'total count':math.ceil(counts/1000),'data':serializer.data})


        except Exception as e:
            return HttpResponse(e,status=500)

class SearchPostImportKey(APIView):
    serializer_class = ImportKeySerializer
    search_document = ImportKeyDocument
    def post(self,request):
        now = time.time()
        BOL = request.data.get('BOL',None)
        HOUSE_BILL = request.data.get('HOUSE_BILL',None)
        SUB_HOUSE_BILL = request.data.get('SUB_HOUSE_BILL',None)
        VOYAGE_NUMBER = request.data.get('VOYAGE_NUMBER',None)
        BILL_TYPE = request.data.get('BILL_TYPE',None)
        manifest = request.data.get('BILL_TYPE',None)
        Country_Code = request.data.get('Country_Code',None)
        CARRIER_CODE = request.data.get('CARRIER_CODE',None)
        Actual_Arrival_Date = request.data.get('Actual_Arrival_Date',None)
        Cargo_Description = request.data.get('Cargo_Description',None)
        Consignee_Name = request.data.get('Consignee_Name',None)
        # limit = int(request.data.get('limit',100))
        page = int(request.data.get('page',1))
        status = False
        l = []
        d = {}
        if BOL:
            query=BOL
            field ='BOL' 
            l.append(Q('match',BOL=query))
            d['BOL']=query
            status = True
        if HOUSE_BILL:
            query=HOUSE_BILL
            field = 'HOUSE_BILL' 
            l.append(Q('match',HOUSE_BILL=query))
            status = True
        if SUB_HOUSE_BILL:
            query=SUB_HOUSE_BILL
            field = 'SUB_HOUSE_BILL'
            l.append(Q('match',SUB_HOUSE_BILL=query))
            status = True
        if VOYAGE_NUMBER:
            query=VOYAGE_NUMBER
            field = 'VOYAGE_NUMBER' 
            l.append(Q('match',VOYAGE_NUMBER=query))
            status = True
        if BILL_TYPE:
            query=BILL_TYPE
            field = 'BILL_TYPE'
            l.append(Q('match',BILL_TYPE=query))
            status = True
        if manifest:
            query=manifest
            field = 'manifest'
            l.append(Q('match',manifest=query))
            status = True
        if Country_Code:
            query=Country_Code
            field = 'Country_Code'
            l.append(Q('match',Country_Code=query))
            d['Country_Code']=query
            status = True
        if CARRIER_CODE:
            query=CARRIER_CODE
            field = 'CARRIER_CODE'
            l.append(Q('match',CARRIER_CODE=query))
            status = True
        if Actual_Arrival_Date:
            query=Actual_Arrival_Date
            field = 'Actual_Arrival_Date'
            l.append(Q('match',Actual_Arrival_Date=query))
            status = True
        if Cargo_Description:
            query=Cargo_Description
            field = 'Cargo_Description'
            l.append(Q('match',Cargo_Description=query))
            status = True
        if Consignee_Name:
            query=Consignee_Name
            field = 'Consignee_Name'
            l.append(Q('match',Consignee_Name=query))
            status = True
        if status:
            # q1 = Q(
            #         'multi_match',
            #         query=query,
            #         fields = [
            #             field
            #         ]
            #     )
            # es = Elasticsearch()
            # res = es.search(
            #     index="importkey", 
            #     body={
            #         "query": {
            #         "match": d
            #     },
            #     "size": 10000
            #     }
            # )
            count = 0

            # return JsonResponse({
            #     'daata':res
            # })
            # print(res['hits'])
            # for key,val in res.items():
            #     if key == 'hits':
            #         # print(val)
            #         for key1,val1 in val.items():
            #             print(key1,'key1')
            #             if 
            # l = []
            d = {}
            c = 0
            # for val in res['hits']['hits']:
            #     # print(val['_source']['piece_count'])
            #     if c==0:
            #         shipper_name = val['_source']['shipper_name']
            #         d[shipper_name] = val['_source']['piece_count']
            #     else:
            #         shipper_name = val['_source']['shipper_name']
            #         if shipper_name in d:
            #             val = d[shipper_name]
            #             val = val + val['_source']['piece_count']
            #         else:
            #             shipper_name = val['_source']['shipper_name']
            #             d[shipper_name] = val['_source']['piece_count']

            # print(d,'d')
            q2 = Q('bool',must=l)
            s = self.search_document.search().query(q2)
            count = s.count()
            skip_count =50
            if page>1:
                start = page*skip_count
                end = start+skip_count
                s2 = self.search_document.search().query(q2)[start:end]
                serializer = self.serializer_class(s2, many=True)
                return JsonResponse({'total rows':count,'total page':math.ceil(count/skip_count),'Data Per Page':skip_count,'page':page,'data':serializer.data})            

            else:
                s2 = self.search_document.search().query(q2)[:skip_count]
                serializer = self.serializer_class(s2, many=True)
                return JsonResponse({'total rows':count,'total page':math.ceil(count/skip_count),'Data Per Page':skip_count,'page':1,'data':serializer.data})            


            if page:
              start = page*1000  
              end = start+1000
              search = self.search_document.search().query(q1)[start:end]
            else:
              search = self.search_document.search().query(q1)[:1000]
                                                                                                                                
            response = search.execute()
            serializer = self.serializer_class(response, many=True)
            # return HttpResponse(response)
            return JsonResponse({'Total Rows':s.count(),'total count':math.ceil(s.count()/1000),'page':page,'data':serializer.data})
        else:
            return HttpResponse('No Keyword Sent')


class GetSeller(APIView):
    serializer_class = ImportKeySerializer
    search_document = ImportKeyDocument
                                                                     
    def post(self,request):
          print('HAHAHA')
          es = Elasticsearch()
          print('NNN')
          page = es.search(
          index = 'importkey',
        #   doc_type = '_source',
          scroll = '3m',
        #   search_type = 'scan',
          size = 100000,
          body = {
            # Your query's body
            })
          print('NPO')
          sid = page['_scroll_id']
          scroll_size = page['hits']['total']
          print(scroll_size,'scroll_size')
        # Start scrolling
          print(type(scroll_size['value']),'scroll_size_type')
          x = scroll_size['value']
          while (x > 0):
            print ("Scrolling...")
            page = es.scroll(scroll_id = sid, scroll = '3m')
            # Update the scroll ID
            sid = page['_scroll_id']
            # Get the number of results that we returned in the last scroll
            scroll_size = len(page['hits']['hits'])
            print(scroll_size,'scroll_size2')
            # print ("scroll size: ") + str(scroll_size)
            # Do something with the obtained page
          return HttpResponse('hello')






        








# tech_ids = ['qwe1', 'qwe2', 'qwe3', 'qwe4', 'qwe5', 'qwe6', 'qwe7']
# {
#   "query": {
#     "bool": {
#       "must": [
#         {
#           "match": {
#             "detail": "calci"
#           }
#         },
#         {
#           "bool": {
#             "should": 
#               [{
#                 "match_phrase": { "tech_id": tid }
#               } for tid in tech_ids]
#           }
#         }
#       ]
#     }
#   }
# }




# GET /_mget
# {
#   "docs": [
#     {
#       "_index": "importkey",
#       "_id": "4870000"
#     },
#     {
#       "_index": "my-index-000001",
#       "_id": "2"
#     }
#   ]
# }



# Shipment
# Buyer
# Suppiler


# seller
# buyer
# product
# shipment
# countries
# log
# Recent Activity
# Transaction History
# 77 (User Alert List)
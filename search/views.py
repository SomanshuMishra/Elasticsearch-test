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


class SearchImportKey(APIView,LimitOffsetPagination):
    serializer_class = ImportKeySerializer
    search_document = ImportKeyDocument
    def get(self,request):
        try:
            # print(request.GET['q'])
            query = request.GET['q']
            page = int(request.GET['page'])
            # print(query,page)
            q = Q(
                'multi_match',
                query=query,
                fields = [
                    'BOL',
                    'HOUSE_BILL',
                    'BILL_TYPE',
                    'Country_Code',
                    'Weight_Unit',
                    'Cargo_Description'
                ],
                fuzziness = "AUTO"
            )
            # start  = request.data.get('page',None)
            search = self.search_document.search().query(q)[:100]
            counts = search.count()
            # print(counts)
            if page>1:
                start = page*100
                end = start+100
                search = self.search_document.search().query(q)[start:end]
                

            response = search.execute()
            # s = self.importkey_serializer(response,many=True)
            # results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(response, many=True)
            return JsonResponse({'Total Rows':counts,'total count':math.ceil(counts/100),'data':serializer.data})


        except Exception as e:
            return HttpResponse(e,status=500)

class SearchPostImportKey(APIView):
    serializer_class = ImportKeySerializer
    search_document = ImportKeyDocument
    def post(self,request):
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
        # limit = int(request.data.get('limit',100))
        page = int(request.data.get('page',1))
        status = False
        l = []
        if BOL:
            query=BOL
            field ='BOL' 
            l.append(Q('match',BOL=query))
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
        if status:
            q1 = Q(
                    'multi_match',
                    query=query,
                    fields = [
                        field
                    ]
                )
            
            # print(l,'l')
            q2 = Q('bool',must=l)
            s = self.search_document.search().query(q2)
            if page>1:
                start = page*1000
                end = start+1000
                s2 = self.search_document.search().query(q2)[start:end]
                serializer = self.serializer_class(s2, many=True)
                return JsonResponse({'Total Rows':s.count(),'total count':math.ceil(s.count()/1000),'page':page,'data':serializer.data})            

            else:
                s2 = self.search_document.search().query(q2)[:1000]
                serializer = self.serializer_class(s2, many=True)
                return JsonResponse({'Total Rows':s.count(),'total count':math.ceil(s.count()/1000),'page':1,'data':serializer.data})            


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
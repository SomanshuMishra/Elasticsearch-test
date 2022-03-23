from re import search
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
# Create your views here.


class SearchImportKey(APIView,LimitOffsetPagination):
    serializer_class = ImportKeySerializer
    search_document = ImportKeyDocument
    def get(self,request,query):
        try:
            print('here')
            q = Q(
                'multi_match',
                query=query,
                fields = [
                    'id',
                    'BOL',
                    'HOUSE_BILL',
                    'BILL_TYPE',
                    'Country_Code',
                    'Weight_Unit'
                ]
            )

            search = self.search_document.search().query(q)
            response = search.execute()
            # s = self.importkey_serializer(response,many=True)
            # results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(response, many=True)
            return JsonResponse(serializer.data,safe=False)
            return self.get_paginated_response(serializer.data)
            # return JsonResponse(response,safe=False)
            # results = self.paginate_queryset(response,request,view=self)
            # serializer = self.importkey_serializer(response,many=True)
            # return self.get_paginated_response(serializer.data)


        except Exception as e:
            return HttpResponse(e,status=500)

class SearchPostImportKey(APIView):
    serializer_class = ImportKeySerializer
    search_document = ImportKeyDocument
    def post(self,request):
        BOL = request.data.get('BOL',None)
        HOUSE_BILL = request.data.get('HOUSE_BILL',None)
        Country_Code = request.data.get('Country_Code',None)
        limit = int(request.data.get('limit',100))
        page = int(request.data.get('page',1))
        start = page*1000
        end = start+1000
        status = True
        all_val = {}
        if BOL:
            query=BOL
            field ='BOL'
            all_val[field] = query 
        if HOUSE_BILL:
            query=HOUSE_BILL
            field = 'HOUSE_BILL'
            all_val[field] = query 
        if Country_Code:
            query=Country_Code
            field = 'Country_Code'
            all_val[field] = query 
        else:
            query=''
            field = ''
            status = False
        if status:
            # print(query,'query')
            # q = Q(
            #     # 'bool',
            #     # "size": 10,
            #     "query":{
            #         "bool": {
            #             for key ,val in all_val.items():
            #                 "must" : {
            #                     "match" : {key:val}
            #                 },
            #         }
            #     }
            #     must=[
            #         Q('match', Country_Code=query),
            #     ],
            #     minimum_should_match=1)
            q1 = Q(
                    'multi_match',
                    # size = 100,
                    query=query,
                    fields = [
                        field
                    ]
                )
            s = self.search_document.search().query(q1)
            print(s.count())
            import math
            search = self.search_document.search().query(q1)[start:end]
            response = search.execute()
            serializer = self.serializer_class(response, many=True)
            return JsonResponse({'total count':math.ceil(s.count()/100),'page':page,'data':serializer.data})
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
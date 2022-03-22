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
            print(search)
            response = search.execute()
            print(response)
            x = {'response':response}
            # s = self.importkey_serializer(response,many=True)
            results = self.paginate_queryset(response, request, view=self)
            print(results)
            serializer = self.serializer_class(response, many=True)
            print(serializer.data)
            return JsonResponse(serializer.data,safe=False)
            return self.get_paginated_response(serializer.data)
            # return JsonResponse(response,safe=False)
            # results = self.paginate_queryset(response,request,view=self)
            # serializer = self.importkey_serializer(response,many=True)
            # return self.get_paginated_response(serializer.data)


        except Exception as e:
            return HttpResponse(e,status=500)



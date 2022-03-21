from dataclasses import field
from turtle import mode
from rest_framework import serializers
from search.models import importkey

class ImportKeySerializer(serializers.ModelSerializer):
    print('herererer')
    # key = 
    class Meta:
        model = importkey
        # fields = [
        #     'BOL',
        #     'HOUSE_BILL',
        #     'BILL_TYPE',
        # ]
        fields = '__all__'
        read_only = True
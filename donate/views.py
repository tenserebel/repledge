from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers
from .serializers import donateSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json

from .models import donate
# Create your views here.

@api_view(["GET","POST"])
def index(request):
    if request.method == 'GET':
        serializer = donateSerializer(donate.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = donateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def details(request, pk):
    try: 
        donation = donate.objects.get(pk=pk)

    except donate.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = donateSerializer(donation)
        return Response(serializer.data) 
    
    elif request.method == 'PUT': 
        serializer = donateSerializer(donation, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

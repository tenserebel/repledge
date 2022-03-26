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
        serializer1 = donateSerializer(donate.objects.all(), many=True)
        return Response(serializer1.data)

    elif request.method == 'POST':
        serializer1 = donateSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.validated_data['location_link'] = f"https://www.google.com/maps/place/{serializer1.validated_data['location']}"
            # serializer1.objects.location_link = f"https://www.google.com/maps/place/{serializer1.objects.location}"
            serializer1.save()

            return Response(serializer1.data, status=status.HTTP_201_CREATED)

        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

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
            serializer.validated_data['location_link'] = f"https://www.google.com/maps/place/{serializer.validated_data['location']}"
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': 
        donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



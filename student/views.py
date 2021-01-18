from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import *
from .serializers import *

class StudentView(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            pk = pk
            return StudentDetails.objects.get(pk=pk)
        except StudentDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        print(request.data)
        if pk:
            response = []
            
            data = StudentDetails.objects.filter(id=pk)
            serializer = StudentDetailSerializer(data, many=True)
            if data:
                response = serializer.data
            return Response(response)
            # return Response({"data":response}, status=status.HTTP_400_BAD_REQUEST)

        else:
            response = []
            data = StudentDetails.objects.all().order_by('-pk')
            print(data)
            serializer = StudentDetailSerializer(data, many=True)
            if data:
                response = serializer.data
            return Response(response)

    def post(self, request, pk=None):
        print(request.data)
        serializer = StudentDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            return Response({"data":serializer.data})

        return Response({"msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        instance = self.get_object(pk)
        print(instance)
        serializer = StudentDetailSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({"data":serializer.data})
        return Response({"msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response({"msg":"Deleted"})




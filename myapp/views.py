from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django_restql.mixins import DynamicFieldsMixin
from rest_framework.response import Response
from myapp.models import *

class UserViewSet(APIView):
    def get(self,request):
        query = request.GET['query'][1:-1].split(',')
        start = int(request.GET['start'])
        end = start + 20
        totalobj = Book.objects.all().count()
        if start > totalobj-1:
            return Response({'status':False,'message':'invalid index'})

        else:
            queryPattern = ['id','title', 'author', 'year_published', 'review', 'Super_Admin_Id']
            for j in queryPattern:
                if not j in query:
                    return Response({'status':False,'message':'invalid query parameter'})

            queryset = Book.objects.values(*query)[start:]
            print("objlength is ",len(queryset))
            return Response({'status':True,'data':queryset,'end':end,'total':totalobj})

    
    
    def post(self,request):
        for i in range(7000):
            print("index===>",i)
            Book(title = "TECH",author = "SHAKEEB",year_published = "1998",review = 4).save()
        return Response({"message":"save"})

        

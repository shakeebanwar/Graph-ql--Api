from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django_restql.mixins import DynamicFieldsMixin
from rest_framework.response import Response
from myapp.models import *


def queryParameter(query):
  count = 0
  queryPattern = ['id','title', 'author', 'year_published', 'review', 'Super_Admin_Id']
  for j in queryPattern:
      
      for k in query:
        if j == k:
          count = count + 1
        

  if count == len(query): 
    return True

  else:
      return False


class UserViewSet(APIView):
    def get(self,request):
       

        ###Key Validation
        if 'query' in request.GET and 'start' in request.GET:
            query = request.GET['query'][1:-1].split(',')
            start = int(request.GET['start'])
            end = start + 20
            totalobj = Book.objects.all().count()
            if start > totalobj-1:
                return Response({'status':False,'message':'invalid index'})

            else:
                queryPattern = ['id','title', 'author', 'year_published', 'review', 'Super_Admin_Id']
                status = queryParameter(query)
                if not status:        
                    return Response({'status':False,'message':'invalid query parameter'})
                
                else:
                    queryset = Book.objects.values(*query)[start:end]
                    return Response({'status':True,'data':queryset,'end':end,'total':totalobj})
        else:
            return Response({'status':False,'message':'query or start key is required'})
    
    
    
    
    
    def post(self,request):
        for i in range(7000):
            print("index===>",i)
            Book(title = "TECH",author = "SHAKEEB",year_published = "1998",review = 4).save()
        return Response({"message":"save"})

        

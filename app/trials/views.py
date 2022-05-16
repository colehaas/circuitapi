from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import IdentificationModule
from .serializers import IdentificiationModuleSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
import requests
import json

baseurl = "https://clinicaltrials.gov/api/"

def CTAPI_FullStudy(request):
    if request.method == 'POST':
        search = json.load(request)['Search']
        if search == 'TRUE':
            expr = json.load(request)['Expr']
            url = baseurl + "query/full_studies?expr={}&min_rnk=1&max_rnk=&fmt=json".format(expr)
            response = requests.request("GET", url)
            data = response.json()
            trialdata = data.Study[0]
            return JsonResponse({'success' : 'sucess'})
    return



class Studies(viewsets.ModelViewSet):
    serializer_class = IdentificiationModuleSerializer
    queryset = IdentificationModule.objects.all()

 
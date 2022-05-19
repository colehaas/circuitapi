from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import IdentificationModule
from .serializers import IdentificiationModuleSerializer, Myserializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
import json

baseurl = "https://clinicaltrials.gov/api/"

def addStudy(request):
    if request.method == 'POST':
        data =  json.load(request)
        method = data["method"]
        NCTId = data["NCTId"]
        print(method)
        print(NCTId)
        if method == "DELETE":
            res = IdentificationModule.objects.filter(NCTId=NCTId).delete()
            print(res)
        elif method == "UPDATE":
            pass
        elif method == "POST":
            #MAKE SURE NCTID IS NOT IN DB
            print(NCTId)
            url = baseurl + "query/full_studies?expr={}&min_rnk=1&max_rnk=1&fmt=json".format(NCTId)
            response = requests.request("GET", url)
            data = response.json()["FullStudiesResponse"]["FullStudies"][0]["Study"]
            section = data["ProtocolSection"]
            module = section["IdentificationModule"]
            trial = IdentificationModule.objects.create(NCTId = NCTId)
            trial.BriefTitle = module["BriefTitle"]
            trial.OfficialTitle = module["OfficialTitle"]
            trial.save()
        return JsonResponse({'success' : 'sucess'})
    return JsonResponse({'success' : 'failure'})



class Studies(viewsets.ModelViewSet):
    serializer_class = IdentificiationModuleSerializer
    queryset = IdentificationModule.objects.all()

@api_view()
def preview(request, expr):
    url = baseurl + "query/full_studies?expr={}&min_rnk=1&max_rnk=10&fmt=json".format(expr)
    response = requests.request("GET", url)
    data = response.json()["FullStudiesResponse"]
    #my_serializer = Myserializer(data=data, many=True)
    #my_serializer.is_valid(True)
    return Response(data)
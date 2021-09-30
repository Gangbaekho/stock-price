from doomoolmori.serializers import DoomoolmoriSerializer
from django.shortcuts import render
from doomoolmori.serializers import DoomoolmoriSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from datetime import datetime 

class DoomoolmoriAPI(APIView):
    def post(self, request, format=None):
        serializer = DoomoolmoriSerializer(data=request.data)
        if serializer.is_valid():
            ticker = serializer.data["ticker"]
            date_from = serializer.data["date_from"]
            date_to = serializer.data["date_to"]

            print(ticker, date_from, date_to)
            url = f"https://rest.yahoofinanceapi.com/v8/finance/chart/{ticker}"

            
            querystring = {"range":"1y","interval":"1d","region":"US","ticker":ticker}

            headers = {
                'x-api-key': "GLlnqxSQh372hIBoSLMIj9S9fH2rSPOs7XjaVolf"
                }

            now = datetime.now()
            date_from_object = datetime.strptime(date_from, '%Y-%m-%d').date()
            date_to_object = datetime.strptime(date_to, '%Y-%m-%d').date()
            

            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.json())
            print(len(response.json()["chart"]["result"][0]["timestamp"]))
            # index 찾는 방법
            # response.json()["chart"]["result"][0]["timestamp"].index('2021-03-25T22:30:00')
            for time in response.json()["chart"]["result"][0]["timestamp"]:
                readable = datetime.fromtimestamp(time).isoformat()
                print(readable)
                
            return Response(response.json(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

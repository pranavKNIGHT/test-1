from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']["test_col"]

class TodoListView(APIView):
    def get(self, request):
        todo= db.find()
        # db.delete_one({"title":"Walk 30min"})
        data = []
        data = list(data)
        for post in todo:
            data.append({'title':post["title"]})
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.method == 'POST':
            post = db.insert_one(request.data)
            return Response({'working'}, status=status.HTTP_200_OK)

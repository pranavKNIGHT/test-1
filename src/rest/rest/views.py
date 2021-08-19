from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']

class TodoListView(APIView):
    def get(self, request):
        posts = db.posts
        data = []
        data = list(data)
        self.__todo = posts.find()
        # db.dropDatabase()
        # posts.delete_one({"title":"charge the phone"})
        # posts.delete_one({"title":"walk 45 mins"})
        # posts.delete_one({"title":"w2"})
        # posts.delete_one({"title":"w3"})
        # posts.delete_one({"title":"todo"})
        for post in self.__todo:
            data.append({'title':post["title"]})
        seen = set()
        self.__newArray = []
        for element in data:
            key = tuple(element.items())
            if key not in seen:
                seen.add(key)
                self.__newArray.append(element)
        return Response(self.__newArray, status=status.HTTP_200_OK)
        
    def post(self, request):
        posts = db.posts
        if request.method == 'POST':
            posts.insert_one(request.data).inserted_id
            return Response('working',status=status.HTTP_200_OK)

    


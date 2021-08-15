from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']

collection = db.test_collection
#getting a database from mongo
posts = db.posts
data = []

#to insert a document 

class TodoListView(APIView):
    
    def get(self, request):
        #self parameter is a reference to the current instance of the class
        global data
        data = list(data)
        global posts
        todo = posts.find()
        # return todo elements in the collection
        for post in todo:
            data.append({'title':post["title"]})
        seen = set()
        newArray = []
        for element in data:
            key = tuple(element.items())
            if key not in seen:
                seen.add(key)
                newArray.append(element)
        return Response(newArray, status=status.HTTP_200_OK)
        
        # Implement this method - return all todo items from db instance above.
        # return Response({}, status=status.HTTP_200_OK)
        
    def post(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        # return Response({}, status=status.HTTP_200_OK)
        global posts
        
        
        if request.method == 'POST':
            posts.insert_one(request.data).inserted_id
        
            return Response('OK!',status=status.HTTP_200_OK)
    
        return Response("error", status=status.HTTP_400_BAD_REQUEST)


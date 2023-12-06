from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def projects(request):
    return Response("List of projects",  status=status.HTTP_200_OK)
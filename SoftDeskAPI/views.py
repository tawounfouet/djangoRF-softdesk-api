from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Comment, Contributor, Issue, Project
from .serializers import (CommentSerializer, ContributorSerializer,
                          IssueSerializer, ProjectSerializer)

from .permissions import IsOwnerOrReadOnly

# @api_view()
# def projects(request):
#     return Response("List of projects",  status=status.HTTP_200_OK)


# class ProjectViewSet(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny, IsOwnerOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

 

class ContributorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

 
    

class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = IssueSerializer

 

class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

 
    
class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


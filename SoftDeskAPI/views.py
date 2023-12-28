from django.shortcuts import render
from django.http import QueryDict
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .models import Comment, Contributor, Issue, Project
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, ContributorSerializer,
                          IssueSerializer, ProjectSerializer)

# @api_view()
# def projects(request):
#     return Response("List of projects",  status=status.HTTP_200_OK)


# class ProjectViewSet(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    #permission_classes = [AllowAny, IsOwnerOrReadOnly]
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


    def create(self, request, *args, **kwargs):
        # Créez une copie mutable de request.data
        data = QueryDict(request.data.urlencode(), mutable=True)
        # Ajoutez l'auteur comme utilisateur connecté
        data['author'] = request.user.id

        # Utilisez le serializer avec les données modifiées
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)
        serializer.save(author=request.user)

        # Obtenez les en-têtes de réponse
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    

    

class ContributorViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    permission_classes = [IsAuthenticated]
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    # redefinir la éthode get_queryset pour les contributeurs d'un projet
    # definir les queryset pour recuperer 




class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = IssueSerializer

    def create(self, request, *args, **kwargs):
        # Créez une copie mutable de request.data
        data = QueryDict(request.data.urlencode(), mutable=True)
        # Ajoutez l'auteur comme utilisateur connecté
        data['author'] = request.user.id

        # Utilisez le serializer avec les données modifiées
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)
        serializer.save(author=request.user)

        # Obtenez les en-têtes de réponse
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    # def perform_create(self, serializer):
    #     # Assurez-vous que l'utilisateur est authentifié
    #     if self.request.user.is_authenticated:
    #         # Spécifiez l'auteur de l'issue comme l'utilisateur actuel
    #         serializer.save(author=self.request.user)
    #     else:
    #         # Gérez le cas où l'utilisateur n'est pas authentifié
    #         raise PermissionDenied(detail='Authentication required')


 

class IssueViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

 
    
class CommentViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


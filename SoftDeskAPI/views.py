from django.http import QueryDict
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import (AllowAny, BasePermission,
                                        IsAuthenticated)
from rest_framework.response import Response

from .models import Comment, Contributor, Issue, Project
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, ContributorSerializer,
                          IssueSerializer, ProjectSerializer)


class IsAuthorOrReadOnly(BasePermission):
    """
    Permission personnalisée pour s'assurer que seul l'auteur peut modifier ou supprimer la ressource.
    """

    def has_object_permission(self, request, view, obj):
        # Permettre les méthodes GET, HEAD ou OPTIONS (lecture de la ressource).
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Sinon, vérifier si l'utilisateur est l'auteur de la ressource.
        return obj.author == request.user

class IsContributorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Contributor.objects.filter(contributor=request.user).exists()





# @api_view()
# def projects(request):
#     return Response("List of projects",  status=status.HTTP_200_OK)


# class ProjectViewSet(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class ProjectViewSet(viewsets.ModelViewSet):
#     #permission_classes = [AllowAny, IsOwnerOrReadOnly]
#     permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsContributorOrReadOnly]
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

#     # restreindre le queryset a la liste des projets auquel l'utilisateur est contributeur
#     def get_queryset(self):
#         user = self.request.user
#         author_id = self.request.query_params.get('author_id')

#         if author_id:
#             # Filtrer les projets par auteur (exemple : author_id passé en paramètre d'URL) # /api/softdesk/projects/?author_id=1
#             return Project.objects.filter(author__id=author_id)

#         # Filtrer les projets en fonction de la relation avec le contributeur
#         return Project.objects.filter(contributors=user)
    
#     # def get_queryset(self):
#     #     return Project.objects.filter(contributors=self.request.user)

#     def perform_create(self, serializer):
#         # Définir l'auteur comme l'utilisateur actuel
#         serializer.save(author=self.request.user)

    


    # def create(self, request, *args, **kwargs):
    #     # Créez une copie mutable de request.data
    #     data = QueryDict(request.data.urlencode(), mutable=True)
    #     # Ajoutez l'auteur comme utilisateur connecté
    #     data['author'] = request.user.id

    #     # Utilisez le serializer avec les données modifiées
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     #self.perform_create(serializer)
    #     serializer.save(author=request.user)

    #     # Obtenez les en-têtes de réponse
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class IsOwnerOrContributorOrReadOnly(BasePermission):
    """
     Object-level permission to only allow owners of an object to edit/delete it.
     Assumes the model instance has an `author` attribute.
     Uers who are contributors can access in read-only mode
    """

    message = "Vous devez être contributeur pour accéder au project et seul l'auteur du projet peut le modifier ou le supprimer."

    def has_permission(self, request, view):
        print(f"\nDEBUG: Action dans has_object_permission: {view.action}\n")
        return True
    
    def has_object_permission(self, request, view, obj):
        # print("has_object_permission", view.action)
        # print("view name", view.get_view_name())
        # print(f"\nDEBUG: Action dans has_object_permission: {view.action}\n")
        # print(f"obj author: {obj.author}")
        # print(f"request user: {request.user}")


        # Author can do anything he is the boss (Instance must have an attribute named `author`)
        if obj.author == request.user:
            return True
        
        if view.action == 'retrieve':
            # Only contributors of the project can read it (Instance must have an attribute named `contributors`)
            contributors = [contrib.contributor for contrib in Contributor.objects.filter(project=obj)] # contributions = related_name in Contributor model
            return request.user in contributors
            
        # if you are not the author and you are not a contributor, you can't do anything
        # if you are not the author or a contributor in read-only mode(retrieve an object) get out of here
        return False
    



class ProjectViewSet(viewsets.ModelViewSet):
    """View to manage project"""

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrContributorOrReadOnly]

    def get_queryset(self):
        """Return the project were the user is the author or a contributor """
        user = self.request.user
        
        
        if self.action == "list":
                # if the user is not the author of the project, he can only see the projects where he is a contributor
                return user.contributions.all()
        
        # permet d'avoir un message issue de la permission si l'utilisateur n'est pas author ou contributeur
        return Project.objects.all()


class ContributorViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    permission_classes = [IsAuthenticated, IsContributorOrReadOnly]
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

     
     # recupérerer plutot le kwarg (a partir du project pk) pour faire les filtre
    def get_queryset(self):
        # Filtrer les contributeurs par projet (exemple : project_id passé en paramètre d'URL) # /api/softdesk/contributors/?project_id=1
        project_id = self.request.query_params.get('project_id')
        if project_id:
            return Contributor.objects.filter(project__id=project_id)
        return Contributor.objects.all()

    # def perform_create(self, serializer):
    #     # Définir l'auteur comme l'utilisateur actuel
    #     serializer.save(contributor=self.request.user)
  

class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsContributorOrReadOnly]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_queryset(self):
        # Filtrer les problèmes/issue par projet (exemple : project_id passé en paramètre d'URL) # /api/softdesk/issues/?project_id=1
        project_id = self.request.query_params.get('project_id')
        if project_id:
            return Issue.objects.filter(project__id=project_id)
        return Issue.objects.all()

    
    def perform_create(self, serializer):
        # Vérifier si l'utilisateur est contributeur du projet associé à l'issue
        project_id = self.request.data.get('project')
        if not Contributor.objects.filter(contributor=self.request.user, project__id=project_id).exists():
            raise PermissionDenied("Vous devez être contributeur pour créer une issue.")
         # Définir l'auteur comme l'utilisateur actuel
        serializer.save(author=self.request.user)
 
    
class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        user = self.request.user
        issue_id = self.request.query_params.get('issue_id')

        if issue_id:
            # Filtrer les commentaires par problème (exemple : issue_id passé en paramètre d'URL) # /api/softdesk/comments/?issue_id=1
            return Comment.objects.filter(issue__id=issue_id)

        # Filtrer les commentaires en fonction de la relation avec le projet
        return Comment.objects.filter(issue__project__contributors=user)


    def perform_create(self, serializer):
        # Vérifier si l'utilisateur est contributeur du projet associé à l'issue de commentaire
        issue_id = self.request.data.get('issue')
        project_id = Issue.objects.get(id=issue_id).project.id
        if not Contributor.objects.filter(contributor=self.request.user, project__id=project_id).exists():
            raise PermissionDenied("Vous devez être contributeur pour créer un commentaire.")
        serializer.save(author=self.request.user)
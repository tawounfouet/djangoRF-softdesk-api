
from rest_framework import permissions
from rest_framework.permissions import BasePermission

from .models import Contributor
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


class IsContributorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        project_id = view.kwargs.get('project_pk')
        return Contributor.objects.filter(contributor=request.user, project=project_id).exists()


class IsOwnerOrContributorOrReadOnly(BasePermission):
    """
     Object-level permission to only allow owners of an object to edit/delete it.
     Assumes the model instance has an `author` attribute.
     Uers who are contributors can access in read-only mode
    """

    message = "Vous devez être contributeur pour accéder au project et seul l'auteur du projet peut le modifier ou le supprimer."

    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):

        # Author can do anything he is the boss (Instance must have an attribute named `author`)
        if obj.author == request.user:
            return True
        
        if view.action == 'retrieve':
            # Only contributors of the project can read it (Instance must have an attribute named `contributors`)
            contributors = [contrib.contributor for contrib in Contributor.objects.filter(project=obj)] # contributions = related_name in Contributor model
            return request.user in contributors
            
        return False
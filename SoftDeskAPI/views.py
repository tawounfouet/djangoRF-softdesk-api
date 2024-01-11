from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Comment, Contributor, Issue, Project
from .permissions import (
    IsAuthorOrReadOnly,
    IsContributorOrReadOnly,
    IsOwnerOrContributorOrReadOnly,
)
from .serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectSerializer,
)


class ProjectViewSet(viewsets.ModelViewSet):
    """View to manage project"""

    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrContributorOrReadOnly,
        IsContributorOrReadOnly,
        IsAuthorOrReadOnly,
    ]

    def get_queryset(self):
        """Return the project were the user is the author or a contributor"""
        user = self.request.user

        if self.action == "list":
            # if the user is not the author of the project,
            # he can only see the projects where he is a contributor
            return user.contributions.all()

        # permet d'avoir un message issue de la permission
        # si l'utilisateur n'est pas author ou contributeur
        return Project.objects.all()

    def perform_create(self, serializer):
        """Affect the author(connected user) automatically"""
        serializer.save(author=self.request.user)


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [
        IsAuthenticated,
        IsContributorOrReadOnly,
        IsOwnerOrContributorOrReadOnly,
        IsAuthorOrReadOnly,
    ]

    def get_queryset(self):
        project_id = self.kwargs.get("project_pk")
        get_object_or_404(Project, pk=project_id)

        queryset = Contributor.objects.filter(project=project_id)
        return queryset

    def perform_create(self, serializer):
        project_id = self.kwargs.get("project_pk")
        project = get_object_or_404(Project, pk=project_id)
        serializer.save(contributor=self.request.user, project=project)


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, IsContributorOrReadOnly]

    def get_queryset(self):
        """Return the project issues were from the project_pk parameter"""
        # check if the project exists
        project_id = self.kwargs.get("project_pk")
        get_object_or_404(Project, pk=project_id)

        queryset = Issue.objects.filter(project=project_id)
        return queryset

    def perform_create(self, serializer):
        project_id = self.kwargs.get("project_pk")
        project = get_object_or_404(Project, pk=project_id)
        serializer.save(author=self.request.user, project=project)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        issue_id = self.kwargs.get("issue_pk")
        issue = get_object_or_404(Issue, id=issue_id)

        return Comment.objects.filter(issue=issue)

    def perform_create(self, serializer):
        """Affect the author(connected user) and the issue(from url) automatically"""
        issue_id = self.kwargs.get("issue_pk")
        issue = get_object_or_404(Issue, id=issue_id)
        serializer.save(author=self.request.user, issue=issue)

from rest_framework import serializers

from .models import Comment, Contributor, Issue, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'author', 'name', 'description', 'project_type', 'created_at', 'contributors')
        read_only_fields = ["author", "contributors"]


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        #fields = '__all__'
        fields = ('id', 'project', 'contributor')


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        #fields = '__all__'
        fields = ('id', 'project','author', 'status', 'priority', 'assigned_user', 'tag', 'created_at')
        read_only_fields = ["author", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ('id', 'issue', 'author', 'content', 'created_at')  
        read_only_fields = ["author", "created_at"]  
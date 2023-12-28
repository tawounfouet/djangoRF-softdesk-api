from rest_framework import serializers

from .models import Comment, Contributor, Issue, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'project_type', 'created_at')
        read_only_fields = ["author", "contributors"]


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        #fields = '__all__'
        fields = ('id', 'contributor', 'project')


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        #fields = '__all__'
        fields = ('id', 'project', 'status', 'priority', 'assigned_user', 'tag', 'author')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        #fields = ('id', 'issue', 'content')    
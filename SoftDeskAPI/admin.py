from django.contrib import admin
from .models import Comment, Issue, Project, Contributor





# class ContributorAdmin(admin.ModelAdmin):
#     list_display = ('user', 'projects')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class IssueAdmin(admin.ModelAdmin):
    list_display = ('project', 'status', 'priority', 'assigned_user', 'tag')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('issue', 'content')


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('contributor', 'project')

admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
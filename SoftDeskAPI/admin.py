from django.contrib import admin

from .models import Comment, Contributor, Issue, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


class IssueAdmin(admin.ModelAdmin):
    list_display = ("project", "priority", "assigned_user", "tag")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("issue", "content", "author")


class ContributorAdmin(admin.ModelAdmin):
    list_display = ("contributor", "project")


admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)

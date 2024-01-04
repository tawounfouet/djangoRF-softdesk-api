# from rest_framework.routers import DefaultRouter


# from . import views

# router = DefaultRouter()
# router.register(r'projects', views.ProjectViewSet, basename='project'),
# router.register(r'contributors', views.ContributorViewSet, basename='contributor')
# router.register(r'issues', views.IssueViewSet, basename='issue')
# router.register(r'comments', views.CommentViewSet, basename='comment')

# urlpatterns = router.urls

# urlpatterns = [
#     path('projects/', views.projects),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from SoftDeskAPI.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

# router = routers.SimpleRouter()
# Le default router  contient en plus du simple router une api qui renvoie tous les liens de liste de routes disponibles
# (Très utilile pour la gestion des routes imbriquées)
router = routers.DefaultRouter()

router.register(r'projects', ProjectViewSet, basename='project'),


# single project path
# /api/softdesk/projects/1/

# /api/softdesk/projects/1/issues/1
# /api/softdesk/projects/1/contributors/
# Add users and issues to a project (project path)
project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
# Add issues to a project (project path)
project_router.register(r'issues', IssueViewSet, basename='project-issues')
project_router.register(r'contributors', ContributorViewSet, basename='project-contributors')


# /api/softdesk/projects/1/issues/1/comments/
issue_router = routers.NestedSimpleRouter(project_router, r'issues', lookup='issue')
issue_router.register(r'comments', CommentViewSet, basename='issue-comments')


#urlpatterns = router.urls + project_router.urls + issues_router.urls



urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls)),
]  



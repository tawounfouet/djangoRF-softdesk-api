from django.urls import include, path
from rest_framework_nested import routers

from SoftDeskAPI.views import (
    CommentViewSet,
    ContributorViewSet,
    IssueViewSet,
    ProjectViewSet,
)

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="project"),


project_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
# Add issues to a project (project path)
project_router.register(r"issues", IssueViewSet, basename="project-issues")
project_router.register(
    r"contributors", ContributorViewSet, basename="project-contributors"
)
# /api/softdesk/projects/1/issues/1/comments/
issue_router = routers.NestedSimpleRouter(project_router, r"issues", lookup="issue")
issue_router.register(r"comments", CommentViewSet, basename="issue-comments")
# urlpatterns = router.urls + project_router.urls + issues_router.urls

urlpatterns = [
    path("", include(router.urls)),
    path("", include(project_router.urls)),
    path("", include(issue_router.urls)),
]

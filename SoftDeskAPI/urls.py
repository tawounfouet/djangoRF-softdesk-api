from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project'),
router.register(r'contributors', views.ContributorViewSet, basename='contributor')
router.register(r'issues', views.IssueViewSet, basename='issue')
router.register(r'comments', views.CommentViewSet, basename='comment')

urlpatterns = router.urls

# urlpatterns = [
#     path('projects/', views.projects),
# ]